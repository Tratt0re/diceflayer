import Lottie from "lottie-react";
import { LoadingAnimation } from "../assets";

/**
 * A React component for displaying a loading overlay with animations when `isLoading` is true.
 * @param {boolean} isLoading - Determines whether the loading overlay should be displayed.
 * @returns {JSX.Element | null} - The JSX element representing the loading overlay or null if not loading.
 */
function LoadingOverlay({ isLoading }) {
    
    if (isLoading) {
        return (
            <div className="loading-overlay">
                <div className="loading-content">
                    {/* You can add loading spinners or text here */}
                    <Lottie animationData={LoadingAnimation} loop={true}/>
                </div>
            </div>
        );
    } else {
        return null;
    }
}

export default LoadingOverlay;