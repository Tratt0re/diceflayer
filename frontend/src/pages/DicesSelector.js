import { MainButton, useHapticFeedback, useShowPopup } from '@vkruglikov/react-telegram-web-app';
import DiceGrid from '../components/DiceGrid';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDiceContext } from '../contexts/DiceContext';
import { appInfo } from "../utils/appInfo";
import ModHeader from '../components/ModHeader';
import LoadingPage from '../components/LoadingPage';


/**
 * A React component for selecting and rolling dice configurations.
 * This component allows users to select different types of dice to roll and initiate the rolling process.
 */
function DicesSelector() {
    
    const navigate = useNavigate()
    const [impactOccurred] = useHapticFeedback()
    const showPopup = useShowPopup()
    const [loading, setLoading] = useState(false)
    const { selectedDices, rollSelectedDices } = useDiceContext()

    // Define the grid of dice configurations
    const dicesGrid = [
        [{ d_type: 2, name: "D2" }, { d_type: 4, name: "D4" }],
        [{ d_type: 6, name: "D6" }, { d_type: 8, name: "D8" }],
        [{ d_type: 10, name: "D10" }, { d_type: 12, name: "D12" }],
        [{ d_type: 20, name: "D10" }, { d_type: 100, name: "D12" }],
    ]

    // Navigate to the results page
    const goToResults = () => {
        navigate(`/results`)
    }

    // Check if there are selected dice configurations to roll
    const thereAreDicesToRoll = () => {
        return Object.keys(selectedDices).length > 0
    }

    // Roll the selected dice configurations
    const rollDices = async () => {
        setLoading(true)
        impactOccurred("medium")
        const response = await rollSelectedDices()
        setLoading(false)
        if (response !== undefined) {
            goToResults()
        } else {
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

    return (
        <>
            {
                loading ?
                    <>
                        <LoadingPage />
                    </>
                    :
                    <>
                        <ModHeader />
                        <div>
                            <DiceGrid dicesGrid={dicesGrid} diceCardType="selector" />
                        </div>
                        <div className="p-2">
                            <p className="hint_text">check the <a href={appInfo.appRepository.url} target="_blank" rel="noopener noreferrer">source</a></p>
                        </div>
                        {
                            thereAreDicesToRoll() ?
                                <MainButton text="Roll dices" onClick={rollDices} />
                                :
                                <></>
                        }
                    </>
            }
        </>
    );
}

export default DicesSelector;