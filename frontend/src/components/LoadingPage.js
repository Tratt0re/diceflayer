import Lottie from "lottie-react";
import { Container } from "reactstrap";
import { LoadingAnimation } from "../assets";

/**
 * A React component for displaying a loading page with an animation.
 * @returns {JSX.Element} - The JSX element representing the loading page.
 */
function LoadingPage() {
    
    return (
        <Container className="loading-page">
            <div>
                <Lottie animationData={LoadingAnimation} loop={true} color="#fff"/>
            </div>
        </Container>
    )
}

export default LoadingPage;