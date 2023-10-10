import React from 'react';
import { D2, D4, D6, D8, D10, D12, D20, D100 } from '../assets';

/**
 * A React component for displaying a dice icon with an optional number.
 * @param {number} diceType - The type of dice (e.g., 2, 4, 6).
 * @param {number} number - The number to display on the dice icon (optional, defaults to the dice type).
 * @param {string} size - The size of the dice icon (e.g., '80px').
 * @param {string} color - The color of the dice icon.
 * @returns {JSX.Element} - The JSX element representing the dice icon.
 */
function DiceIcon({ diceType, number = diceType, size, color }) {
    
    const diceComponents = {
        2: D2,
        4: D4,
        6: D6,
        8: D8,
        10: D10,
        12: D12,
        20: D20,
        100: D100,
    };

    const DiceComponent = diceComponents[diceType];

    if (!DiceComponent) {
        return <h1 className="display-3 text-center text-wieght-bold">{diceType}</h1>;
    }

    // Render the SVG component
    return (
        <div className='dice_icon_container'>
            <div className='dice_number_container' style={{ width: size, height: size }}>
                <p className='dice_number_text'>{number}</p>
            </div>
            <div>
                <DiceComponent width={size} height={size} fill={color} />
            </div>
        </div>
    );
}

export default DiceIcon;