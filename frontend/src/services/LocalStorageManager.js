/**
 * A utility class for managing data in the browser's local storage.
 */
class LocalStorageManager {
    
    /**
     * Save data to local storage.
     *
     * @param {string} key - The key under which to store the data.
     * @param {any} value - The data to be stored (should be JSON serializable).
     */
    static setItem(key, value) {
        localStorage.setItem(key, JSON.stringify(value));
    }

    /**
     * Retrieve data from local storage or set a backup data if the key doesn't exist.
     *
     * @param {string} key - The key to retrieve data from.
     * @param {any} backupData - The backup data to return if the key doesn't exist (default: null).
     * @returns {any} - The retrieved data or the backup data.
     */
    static getItem(key, backupData = null) {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : backupData;
    }

    /**
     * Remove data from local storage.
     *
     * @param {string} key - The key of the data to be removed.
     */
    static removeItem(key) {
        localStorage.removeItem(key);
    }
}

export default LocalStorageManager;