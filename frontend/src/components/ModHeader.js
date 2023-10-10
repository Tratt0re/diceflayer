import { Button, Col, Container, Row } from "reactstrap";
import { useDiceContext } from "../contexts/DiceContext";

/**
 * A React component for setting and displaying a modifier value.
 * @returns {JSX.Element} - The JSX element representing the modifier header.
 */
function ModHeader() {
    
    const { modifier, manageModifier } = useDiceContext()

    const add = () => {
        manageModifier(modifier + 1)
    }

    const subtract = () => {
        manageModifier(modifier - 1)
    }

    return (
        <div className="sticky-header p-2">
            <Container>
                <Row className="justify-content-center">
                    <Col xs="6" className="d-flex align-items-center  p-0 m-0">
                        <p className="p-0 m-0">Set modifier</p>
                    </Col>
                    <Col xs="6" className="d-flex justify-content-between align-items-center">
                        <Button disabled={modifier === 20} color="primary" onClick={add}>+</Button>
                        <h3 className="m-0 p-0">{modifier}</h3>
                        <Button disabled={modifier === -20} color="primary" onClick={subtract}>-</Button>
                    </Col>
                </Row>
            </Container>
        </div>
    );
}

export default ModHeader;