import { Col, Container, Row } from "reactstrap";
import SelectDiceCard from "./SelectDiceCard";
import DiceCard from "./DiceCard";


/**
 * A React component for displaying a grid of dice cards.
 * @param {Array} dicesGrid - An array representing the grid of dice cards.
 * @param {string} diceCardType - The type of dice cards to display ("selector" or "results").
 */
function DiceGrid({ dicesGrid = [], diceCardType = "selector" }) {

    /**
     * Render the grid of dice cards based on the provided data.
     * @returns {JSX.Element} - The JSX element representing the dice grid.
     */
    return (
        <Container>
            {
                dicesGrid.map(((diceRow, idx) => {
                    return (
                        <Row key={`dice-row-${idx}`} className={idx === 0 ? "mb-3 mt-2" : "mb-3"}>
                            {
                                diceRow.map((dice, idx, array) => {
                                    return (
                                        <Col key={`dice-col-${idx}`} xs={`${12 / array.length}`}>
                                            {
                                                diceCardType === "selector" ?
                                                    <SelectDiceCard key={`dice-${idx}`} d_type={dice.d_type} name={dice.name} />
                                                    :
                                                    <DiceCard key={`dice-${idx}`} d_type={dice.d_type} number={dice.last_roll} />
                                            }
                                        </Col>
                                    )
                                })
                            }
                        </Row>
                    )
                }))
            }
        </Container>
    );
}

export default DiceGrid;