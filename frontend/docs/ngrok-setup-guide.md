# Ngrok setup guide

[Ngrok](https://ngrok.com/) is a popular tool for exposing local servers to the internet, which can be handy for testing and sharing your React app during development. This guide will walk you through the steps to run a React app on Ngrok.

>***NOTE: You will need to create a ngrok account to use its services. You can use it for free but each time you will run ngrok on your terminal a different url will be provided to you***

## Prerequisites

Before you begin, make sure you have the following:

- A React app that you want to expose to the internet.
- Node.js and npm installed on your local machine.
- Ngrok installed on your system. You can download it from [Ngrok's official website](https://ngrok.com/download).

## Steps

### 1. Install Ngrok
If you haven't already installed Ngrok, download and install it following the instructions on the [Ngrok download page](https://ngrok.com/download).

### 2. Start Your React App

- Open your terminal and navigate to the directory where your React app is located.

- Start your React development server using the command `npm start`

This will start your app on a local development server, typically at `http://localhost:3000`

### 3. Expose Your Local Server with Ngrok

- In a new terminal window, navigate to the directory where you have Ngrok installed. (_Or just type ngrok in your terminal if you installed it globally on your system_)

- Use the following command to expose your local React app to a public URL: `ngrok http 3000`. If you are using the **Diceflayer app** you can just run in a new terminal window, once reached the project location, `npm run ngrok`

>The `http` command specifies that you're exposing an HTTP server running on port `3000`. Adjust the port number if your React app is running on a different port.

- Ngrok will provide you with a public URL (e.g., `https://your-subdomain.ngrok.io`) that you can use to access your locally hosted React app from anywhere on the internet.

### 4. Link your Telegram Mini App
Now that you are hosting your bot you can use [@BotFather](https://t.me/botfather) to link the menu button of your bot to your mini app.

- Open Telegram and search for  [@BotFather](https://t.me/botfather).
- Use the /mybots command to list your bots.
- Select the bot for which you want to change the menu button URL.
- Choose the "Bot Settings" option.
- Select "Edit Menu" and then "Edit the current commands list."
- Update the command URL for your menu button.

## What's next ?
Now you should be able to access the frontend of the mini app. 

You can still check how to use [Github Pages](./gh-pages-setup-guide.md) to host the mini app for free, or check how to create your very own frontend following the [Develop from zero guide](./develop-from-zero.md).

## Are you lost?
Click [HERE](../README.md) to reach the main documentation page.

