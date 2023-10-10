import { useThemeParams } from "@vkruglikov/react-telegram-web-app";
import { Container, Row } from "reactstrap";
import DiceIcon from "./DiceIcon";

/**
 * A React component for displaying a single dice card.
 * @param {number} d_type - The type of dice.
 * @param {number} number - The number of dice to display.
 */
function DiceCard({ d_type, number }) {

    const [colorScheme, themeParams] = useThemeParams();

    /**
     * Get the color for the dice icon based on the theme parameters.
     * @returns {string} - The color code for the dice icon.
     */
    const getDiceColor = () => {
        return themeParams.text_color ? themeParams.text_color : "#555"
    }

    return (
        <Container className="p-3 dice_container">
            <Row>
                <DiceIcon diceType={d_type} number={number} size={"80px"} color={getDiceColor()} />
            </Row>
        </Container>
    );
}

export default DiceCard;