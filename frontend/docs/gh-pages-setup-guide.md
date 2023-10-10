# GitHub Pages Setup Guide

GitHub Pages is a free hosting service provided by GitHub that allows you to host static websites directly from your GitHub repository. This guide will walk you through the process of hosting your React app on GitHub Pages.

## Prerequisites

Before you begin, make sure you have the following:

- A GitHub account.
- A React app that you want to host.
- Git installed on your local machine.

## Steps

### 1. Create a GitHub Repository
If you don't already have a GitHub repository for your React app, create one by following these steps:
   - Log in to your GitHub account.
   - Click on the "+" icon in the upper right corner and select "New repository."
   - Choose a name for your repository and configure other settings as needed.
   - Click "Create repository."

### 2. Prepare Your React App
Ensure that your React app is ready for deployment. This typically involves running the build process to generate production-ready static files. Use the following command in your app's directory: `npm run build`

### 3. Install `gh-pages` Package
Install the `gh-pages` package as a development dependency in your project. You can do this by running: 

```bash
npm install --save-dev gh-pages
```

### 4. Update `package.json`

4. Open your `package.json` file and add the following lines to the top-level object:

```json
"homepage": "https://<username>.github.io/<repository-name>"
```

Replace `<username>` with your GitHub username and `<repository-name>` with the name of your GitHub repository.

Next, add the following lines to the "scripts" section:

```json
"predeploy": "npm run build",
"deploy": "gh-pages -d build"
```

Your package.json file should now look something like this:

```json
{
  "name": "my-react-app",
  "version": "1.0.0",
  "homepage": "https://<username>.github.io/<repository-name>",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "predeploy": "npm run build",
    "deploy": "gh-pages -d build"
  },
  // ...
}
```
### 5. Deploy Your React App
Now, you're ready to deploy your React app to GitHub Pages. Run the following command: `npm run deploy`

After the deployment is complete go to your repo and check if this is correctly set: 
   - Select the created repository and press on "Settings".
   - Select "Pages" (_it's under "Code and automation" section_)
   - Select "Deploy from branch" choose gh-pages /(root) and then save.

### 6. Access Your Deployed App
After the deployment process is complete, your React app should be accessible at the following URL:
`https://<username>.github.io/<repository-name>`

As before, replace `<username>` with your GitHub username and `<repository-name>` with the name of your GitHub repository.

### 7. Link your Telegram Mini App
Now that you are hosting your bot you can use [@BotFather](https://t.me/botfather) to link the menu button of your bot to your mini app.

- Open Telegram and search for  [@BotFather](https://t.me/botfather).
- Use the /mybots command to list your bots.
- Select the bot for which you want to change the menu button URL.
- Choose the "Bot Settings" option.
- Select "Edit Menu" and then "Edit the current commands list."
- Update the command URL for your menu button.

NOTE: this react project uses `Hash navigation` because github pages only consent to host SPA (Single Page App) or basic websites. In order to make your bot correctly render the react app you will have to use this as url for your Menu Button: 

```html
https://<username>.github.io/<repository-name>/#/
```

As before, replace `<username>` with your GitHub username and `<repository-name>` with the name of your GitHub repository. Notice the `/#/` it is basicly the main route of the app.

### Additional Notes
Whenever you make changes to your React app, repeat steps 2 and 5 to update your deployed app on GitHub Pages.

GitHub Pages may take a few minutes to update after you deploy changes.

>For more advanced configurations or custom domains, consult the [GitHub Pages documentation](https://docs.github.com/en/pages).

## What's next ?
Now you should be able to access the frontend of the mini app. 

You can still check how to use [Ngrok](./ngrok-setup-guide.md) to host the mini app and speed up development, or check how to create your very own frontend following the [Develop from zero guide](./develop-from-zero.md).

## Are you lost?
Click [HERE](../README.md) to reach the main documentation page.