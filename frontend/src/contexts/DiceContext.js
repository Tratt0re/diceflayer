import React, { createContext, useContext, useState } from 'react';
import ApiService from '../services/api';
import { useInitData } from '@vkruglikov/react-telegram-web-app';
import LocalStorageManager from '../services/LocalStorageManager';

// Create a new context
const DiceContext = createContext();

/**
 * A custom hook for accessing the DiceContext.
 * Allows components to access the context's state and functions.
 * @returns {object} - Context value containing state and functions.
 */
export function useDiceContext() {
    return useContext(DiceContext);
}

/**
 * A provider component that wraps the application and provides the DiceContext to child components.
 * Manages state related to dice configuration, rolling, and history.
 * @param {object} props - React component props.
 */
export function DiceProvider({ children }) {
    
    const [initDataUnsafe] = useInitData();
    const [modifier, setModifier] = useState(LocalStorageManager.getItem("modifier", 0));
    const [selectedDices, setSelectedDices] = useState(LocalStorageManager.getItem("selectedDices", {}));
    const [resultDices, setResultDices] = useState(LocalStorageManager.getItem("resultDices", {}));

    /**
     * Manage the selected dice configuration.
     * @param {number} d_type - The type of dice.
     * @param {number} amount - The number of dice of that type to select.
     */
    const manageSelectedDice = (d_type, amount) => {
        const newDicesObj = { ...selectedDices }
        if (amount > 0) {
            newDicesObj[d_type] = amount
        } else {
            delete newDicesObj[d_type]
        }
        setSelectedDices(newDicesObj)
    };

    /**
     * Roll the selected dice configurations and update the resultDices state.
     * @returns {object|undefined} - The rolled dice results or undefined in case of an error.
     */
    const rollSelectedDices = async () => {
        try {
            LocalStorageManager.setItem("modifier", modifier)
            LocalStorageManager.setItem("selectedDices", selectedDices)
            const response = await ApiService.rollDices(initDataUnsafe.user.id, selectedDices, modifier)
            if (response.status === 200) {
                const data = response.data["data"]
                setResultDices(data)
                LocalStorageManager.setItem("resultDices", data)
                return data
            } else {
                return undefined
            }
        } catch (error) {
            console.error(`DiceProvider.rollSelectedDices failed: ${error}`)
            return undefined
        }
    }

    /**
     * Get the amount of selected dice of a specific type.
     * @param {number} d_type - The type of dice.
     * @returns {number} - The number of selected dice of that type.
     */
    const getAmountOfSelectedDice = (d_type) => {
        const amount = selectedDices[d_type]
        return amount ? amount : 0
    }

    /**
     * Manage the modifier value for dice rolls.
     * @param {number} mod - The modifier value to set.
     */
    const manageModifier = (mod) => {
        setModifier(mod)
    }

    /**
     * Calculate the total number of selected dice.
     * @returns {number} - The total number of selected dice.
     */
    const getTotalNumberOfDices = () => {
        let totalNumberOfDices = 0
        Object.keys(selectedDices).forEach(key => {
            totalNumberOfDices += Number(selectedDices[key])
        })
        return totalNumberOfDices
    }

    /**
     * Clear the dice configuration and result history stored in local storage.
     */
    const clearDiceHistory = () => {
        LocalStorageManager.removeItem("selectedDices")
        LocalStorageManager.removeItem("resultDices")
        LocalStorageManager.removeItem("modifier")
    }

    // Context value containing state and functions
    const contextValue = {
        selectedDices,
        resultDices,
        modifier,
        manageSelectedDice,
        rollSelectedDices,
        manageModifier,
        getAmountOfSelectedDice,
        getTotalNumberOfDices,
        clearDiceHistory
    };

    return (
        <DiceContext.Provider value={contextValue}>{children}</DiceContext.Provider>
    );
}