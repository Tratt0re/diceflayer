import { useEffect } from "react";

/**
 * 
 * This hook is designed to execute a function passed as an argument when a component mounts, 
 * similar to the built-in componentDidMount lifecycle method in class components
 * 
 * @param {() => void} func - The function to execute when the component mounts.
 */
const useMountEffect = (func) => {
    // eslint-disable-next-line react-hooks/exhaustive-deps
    useEffect(func, []);
};

export default useMountEffect;