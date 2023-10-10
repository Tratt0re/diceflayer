import packageJson from '../../package.json';

// Extract version, name, and repository information from packageJson
const appVersion = packageJson.version;
const appName = packageJson.name;
const appRepository = packageJson.repository;

// Create an appInfo object containing the extracted information
export const appInfo = {
    appVersion,
    appName,
    appRepository
};