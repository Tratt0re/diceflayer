import axios from "axios"


const API_URL = "https://<your_very_own_url>" // Read the backend documentation to provide an url to this project

/**
 * Class for making API requests related to rolling dice.
 */
export default class ApiService {
    
    /**
     * Send a request to roll dice with the specified parameters.
     *
     * @param {string} user_id - The user ID for the request.
     * @param {string} dices - The dice configuration to roll.
     * @param {number} modifier - The modifier to apply to the roll.
     * @returns {Promise} - A promise that resolves with the API response data.
     */
    static rollDices = (user_id, dices, modifier) => {
        return axios.post(`${API_URL}/bot/roll_dices`, { user_id, dices, modifier });
    }
}