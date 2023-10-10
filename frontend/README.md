# Diceflayer (FE) - Documentation
[Diceflayer](https://t.me/MrDiceflayerBot) is a Telegram Mini App designed to assist users in rolling dices for tabletop games like Dungeons & Dragons.

**This folder contains the frontend code for the Diceflayer telegram mini-app.**

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Telegram Bot](#telegram-bot)
- [Host the Mini App](#host-the-mini-app)
- [Installation](#installation)
- [Usage](#usage)
- [Start from zero](#start-from-zero)
- [License](#license)
- [Full Doc](#full-doc)

## Project Structure
The project is organized as follows:

- 📁 **public**: This folder is the public directory for react app. It contains the `index.html` file, which serves as the entry point for your application.

- 📁 **src**: The `src` directory is the heart of the app, housing all the source code.

    - 📁 **assets**: It contains SVGs representing dice used in the app, and the lottie animation .json used in loading components

    - 📁 **components**: Contians reusable components to enhance code modularity.

    - 📁 **contexts**: The `contexts` directory contains Context Provider logic to handle complex application-wide state and logic.

    - 📁 **services**: Inside the `services` folder, you'll find two important files:

        - 📄 **api.js**: This file handles HTTP requests, allowing the app to communicate with APIs or servers.
        
        - 📄 **LocalStorageManager.js**: The `LocalStorageManager.js` file manages local storage operations, providing functionalities for storing data locally in the user's browser.

    - 📁 **utils**: The `utils` folder houses generic or very specific functions that aren neither component spcific logic nor services. These utilities can be called at any time within the app flow.


## Features

- **Dice Rolling**: Roll a variety of dice, including d2, d4, d6, d8, d10, d12, d20 and d100, with customizable modifiers.
- **Result History**: Keep track of your previous rolls for reference within telegram chat.
- **Telegram Integration**: Seamlessly interact with Telegram components and hooks using the `@vkruglikov/react-telegram-web-app` library.
- **Automatic Deployment**: The project uses `gh-pages` library to automate deployment, along the documentation you can learn more about it.
- **Simplify the development through ngrok service**: The project exposed an npm command to start a ngrok free instance to proxy a public ssl address to local react server and speed up test-while-developing processes.

## Technologies Used

- [**React**](https://react.dev/): A JavaScript library for building user interfaces.
- [**Reactstrap**](https://reactstrap.github.io/): A Bootstrap framework for React that helps create responsive and mobile-friendly web applications.
- [**React Axios**](https://github.com/sheaivey/react-axios): A promise-based HTTP client for making HTTP requests.
- [**Lottie-React**](https://github.com/Gamote/lottie-react): A library for rendering Adobe After Effects animations as React components.
- [**react-telegram-web-app**](https://github.com/vkruglikov/react-telegram-web-app): A library for integrating with Telegram components and hooks.
- [**gh-pages**](https://github.com/tschaub/gh-pages): A tool to deploy your app to GitHub Pages.

## Telegram Bot

>Before going to the installation part, you need to create a **telegram bot** to link this miniapp to. Whether you can run it in your local browser, you will leak the telegram main components that are the core of the project, and the general experience will be ruined. Follow the steps below to create a bot in a quick way.

Check this [Bot Setup Guide](./docs/bot-setup-guide.md) if you are completely new to bots, or if you already know how to do it just open [@BotFather](https://t.me/botfather)


## Host the Mini App
**Github Pages**: 
This project uses Github Pages to host the Mini App, it is a free and easy to set-up tool that let you host a static web page on github servers, check the [Github Pages setup guide](./docs/gh-pages-setup-guide.md) to learn how to integrate it. 

**Ngrok**: You can also run this app through a ngrok tunnel, it is a tool that proxy a temporary public url to your localhost server. Whether it offers a free plan, it is a good choice just for development reason. Check the [Ngrok setup guide](./docs/ngrok-setup-guide.md) to learn how to use it. 

## Installation
> You'll need `node.js` and `react` installed on your machine before starting this project. To know more about them you can check the official guides linked below

- [Node.js Official Guide](https://nodejs.dev/en/learn/)
- [React Official Guide](https://react.dev/learn/installation)


To install all the required libraries, run the following command once in the frontend root folder:
```bash 
npm install
```

Once the app is installed, it will lack a link to the backend. Open the `src/services/api.js` file and add the url that identifies the server on which the backend application is running. 

>If you are here just to check frontend logics don't bother about this step, but you'll have to modify the source code a bit to skip the call to the backend services. In this case you should check the following files`./src/pages/DicesSelector.js` and `./src/contexts/DiceContext.js`.

## Usage

To run the app locally you can use the command below
```bash
npm run start
```

The app will be hosted on react local development server at http://localhost:3000/diceflayer

If you want to host the mini app through Github Pages you will need to deploy your project to github, you can use this one if you want, in that case i suggest you to copy the frontend folder in a new project and start from there. **Make sure to have followed** the [Github Pages setup guide](./docs/gh-pages-setup-guide.md) first.

If you want to just run the project locally but check the telegram functionalities as well, open another terminal, position yourself at the project folder location and run `npm run ngrok`. **Make sure to have followed** the [Ngrok setup guide](./docs/gh-pages-setup-guide.md) first.

## Start from zero
You can check this project and use it for reference to create your very own bot as well. Check the code to discover more about the implementations, i added comments and descriptions to simplify the understanding process.

If you are seeking a more tutorial-like experience to start your own project, i wrote this [Simple development guide](./docs/develop-from-zero.md) that will help you setup a blank frontend mini app using `create-react`

Keep in mind that this is just the **frontend** part of the Mini App, you'll need to check and install also the [backend](../backend/README.md) to have a fully understainding of its logics.

## License
This project is dual-licensed under the **BSD License** and the **MIT License**. You are free to use, modify, and distribute the code. If you fork this project or use it as a base, please remember to cite the original author, [@Tratt0re](https://github.com/Tratt0re), in your documentation.

- [MIT Licence](../MIT_LICENSE)
- [BSD Licence](../BSD3_LICENSE)

## Full Doc
Full documentations legend available [HERE](./docs/README.md)

