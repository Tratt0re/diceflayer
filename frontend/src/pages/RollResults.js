import { useNavigate } from "react-router-dom";
import { MainButton, BackButton, useShowPopup, useHapticFeedback } from '@vkruglikov/react-telegram-web-app';
import DiceGrid from "../components/DiceGrid";
import { useDiceContext } from "../contexts/DiceContext";
import { useEffect, useState } from "react";
import DiceHeader from "../components/DiceHeader";
import LoadingOverlay from "../components/LoadingOveraly";


/**
 * A React component for displaying and interacting with the results of rolled dice configurations.
 * This component displays the rolled dice results, allows re-rolling, and provides navigation options.
 */
function RollResults() {

    const navigate = useNavigate()
    const { resultDices, rollSelectedDices, clearDiceHistory } = useDiceContext()
    const [dicesGrid, setDiceGrid] = useState([])

    const [impactOccurred] = useHapticFeedback()
    const showPopup = useShowPopup()
    const [loading, setLoading] = useState(false)

    // Build the dice grid when resultDices change
    useEffect(() => {
        const new_grid = buildDiceGrid()
        setDiceGrid(new_grid)
    }, [resultDices])

    // Navigate back to the dice selection page
    const goBack = () => {
        clearDiceHistory()
        navigate("/")
    }

    // Roll the currently selected dice configurations
    const rollDices = async () => {
        setLoading(true)
        impactOccurred("medium")
        const response = await rollSelectedDices()
        setLoading(false)
        if (response === undefined) {
            // Show a popup in case of an unexpected error
            const popup_response = await showPopup({
                title: "Unexpected error occurred",
                message: "Diceflayer server got a 1 on constitution saving throw!",
                buttons: [{ id: "0", text: "Cancel" },
                { id: "1", text: "Try again", }]
            })
            // Retry rolling the dice if the user chooses to try again
            if (popup_response === "1") {
                rollDices()
            }
        }
    }

    // Build the dice grid based on the resultDices
    const buildDiceGrid = () => {
        const dices = resultDices["dices"]
        const numberOfRows = Math.ceil(dices.length / 3); // Calculate the number of rows

        const newGrid = Array.from({ length: numberOfRows }, (_, rowIndex) => {
            const startIndex = rowIndex * 3;
            const endIndex = Math.min(startIndex + 3, dices.length);
            const rowDices = dices.slice(startIndex, endIndex);
            return rowDices;
        });

        return newGrid
    }

    return (
        <>
            <LoadingOverlay isLoading={loading} />
            <DiceHeader totalDices={resultDices["total_dices"]} modifier={resultDices["modifier"]} total={resultDices["total"]} />
            <div>
                <DiceGrid dicesGrid={dicesGrid} diceCardType="results" />
            </div>
            <div>
                <MainButton text="Re-Roll dices" onClick={rollDices} />
                <BackButton onClick={goBack} />
            </div>
        </>

    );
}

export default RollResults;