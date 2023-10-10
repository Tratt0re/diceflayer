import { Col, Container, Row } from "reactstrap";

/**
 * A React component for displaying the header of the dice roll results.
 * @param {number} totalDices - The total number of dice rolled.
 * @param {number} modifier - The modifier added to the dice roll (if any).
 * @param {number} total - The total result of the dice roll.
 */
function DiceHeader({ totalDices = 0, modifier = 0, total = 0 }) {

    /**
     * Generate the header components based on the provided data.
     * @returns {JSX.Element} - The JSX element representing the header components.
     */
    const getHeaderComponents = () => {
        if (totalDices === total) { // no modifier present
            return (
                <Col xs="12">
                    <p className="p-0 m-0">Total: <b>{totalDices}</b></p>
                </Col>
            )
        } else { // modifier present
            return (
                <>
                    <Col xs="12" className="d-flex justify-content-between align-items-center">
                        <p className="p-0 m-0">Dices: <b>{totalDices}</b></p>
                        <p className="p-0 m-0">Mod: <b>{modifier > 0 ? `+${modifier}` : modifier}</b></p>
                    </Col>
                    <Col xs="12" className="text-center">
                        <p className="p-0 m-0">Total</p>
                        <p className="display-3 text-center text-wieght-bold p-0 m-0">{total}</p>
                    </Col>
                </>
            )
        }
    }

    return (
        <div className="sticky-header p-2">
            <Container>
                <Row className="justify-content-center">
                    {
                        getHeaderComponents()
                    }
                </Row>
            </Container>
        </div>
    );
}

export default DiceHeader;