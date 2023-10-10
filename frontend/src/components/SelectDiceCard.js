import { useHapticFeedback, useThemeParams } from "@vkruglikov/react-telegram-web-app";
import { useState } from "react";
import { Button, ButtonGroup, Container, Row, Badge } from "reactstrap";
import DiceIcon from "./DiceIcon";
import { useDiceContext } from "../contexts/DiceContext";

/**
 * A React component for selecting the number of a specific type of dice.
 * @param {Object} props - The props for this component.
 * @param {number} props.d_type - The type of dice.
 * @returns {JSX.Element} - The JSX element representing the select dice card.
 */
function SelectDiceCard({ d_type }) {

    const { getTotalNumberOfDices, manageSelectedDice, getAmountOfSelectedDice } = useDiceContext()
    const [colorScheme, themeParams] = useThemeParams();
    const [impactOccurred] = useHapticFeedback()
    const [nDices, setNDices] = useState(getAmountOfSelectedDice(d_type))

    const add = () => {
        const newValue = nDices + 1
        setNDices(newValue)
        manageSelectedDice(d_type, newValue)
        impactOccurred("medium")
    }

    const subtract = () => {
        const newValue = nDices === 0 ? 0 : nDices - 1
        setNDices(newValue)
        manageSelectedDice(d_type, newValue)
        impactOccurred("medium")
    }

    /**
     * Checks if the maximum number of dices (20) has been reached.
     * @returns {boolean} - True if the maximum number is reached, false otherwise.
     */
    const maximumNumberOfDicesReached = () => {
        const totalNumberOfDices = getTotalNumberOfDices()
        return totalNumberOfDices === 20
    }

    /**
     * Gets the color for displaying the dice.
     * @returns {string} - The color value.
     */
    const getDiceColor = () => {
        return themeParams.text_color ? themeParams.text_color : "#555"
    }

    return (
        <Container className="p-3 dice_container" >
            <Row>
                <div className="badged_dice_container">
                    {
                        nDices > 0 ? <Badge className="dice_badge" color="danger">{nDices}</Badge> : <></>
                    }
                    <DiceIcon diceType={d_type} size={"80px"} color={getDiceColor()} />
                </div>
            </Row>
            <Row>
                <ButtonGroup size="sm">
                    {nDices === 0 ? (
                        <Button onClick={add} color="primary" disabled={maximumNumberOfDicesReached()}>
                            Add
                        </Button>
                    ) : (
                        <>
                            <Button onClick={add} color="primary" disabled={maximumNumberOfDicesReached()}>+</Button>
                            <Button onClick={subtract} color="primary">-</Button>
                        </>
                    )}
                </ButtonGroup>
            </Row>
        </Container>
    );
}

export default SelectDiceCard;