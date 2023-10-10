# Diceflayer (BE) - Documentation
[Diceflayer](https://t.me/MrDiceflayerBot) is a Telegram Mini App designed to assist users in rolling dices for tabletop games like Dungeons & Dragons.

**This folder contains the backend code for the Diceflayer telegram mini-app.**

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Telegram Bot](#telegram-bot)
- [Serve the Backend](#serve-the-backend)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Full Doc](#full-doc)

## Project Structure

The project is organized as follows:

- 📂 **api**: Contains the routes builder and the top-level logic for the API.
- 📂 **controller**: Contains controllers to handle complex logic on behalf of the API interface.
- 📂 **core**: Houses some low-level architecture logics.
- 📂 **init**: Contains app initialization logic (e.g., startup and configurations).
- 📂 **model**: Defines data models used in the app.
- 📂 **resources**: Contains the `config.yml` used to handle environment variables.
- 📂 **services**: Contains service classes used by the controllers.
- 📂 **utils**: Houses generic or very specific functions that are neither controllers nor services and can be called at any time within the app flow.

- 📄 `app.py`: The starting point, used to call initialization methods.

This structure helps organize the codebase into distinct functional areas, making it easier to maintain and navigate the project.

## Features

- **Dice Rolling**: Roll a variety of dice, including d2, d4, d6, d8, d10, d12, d20 and d100, with customizable modifiers.
- **Result History**: Keep track of your previous rolls for reference within telegram chat.
- **Classic Bot Experience**: This bot listen for new messages on a webhook and handle them accordingly.
- **Heroku Deployment**: The project uses Heroku for hosting and automatic deployment.
- **Ngrok Deployment**: The project explains how to use ngrok to reverse proxy your localhost and test without the need of deploying your app on a server.

## Technologies Used

- [**Python 3.11.3**](https://www.python.org/downloads/release/python-3113/): Python is a high-level, general-purpose programming language. In this project, Python 3.11.3 is used as the core programming language for developing the backend of the Telegram bot's mini-app.
- [**Flask**](https://flask.palletsprojects.com/en/2.1.x/): Flask is a lightweight and flexible micro web framework for Python. It is used to develop web applications and provides the necessary tools and libraries to create APIs, handle routing, and manage HTTP requests and responses.
- [**Flask-Cors**](https://flask-cors.readthedocs.io/en/latest/): Flask-Cors is a Flask extension that simplifies handling Cross-Origin Resource Sharing (CORS) in Flask applications. It allows you to define which origins are permitted to access your API, making it useful for handling requests from different domains.
- [**Gunicorn**](https://gunicorn.org/): Gunicorn, short for Green Unicorn, is a production-ready HTTP server for running Python applications. It is often used as a WSGI HTTP server to serve Flask applications in a production environment.
- [**python-dotenv**](https://pypi.org/project/python-dotenv/): python-dotenv is a Python library that helps manage environment variables from a .env file. It simplifies the process of setting configuration variables for your application, making it easier to handle configuration changes across different environments.
- [**PyYAML**](https://pyyaml.org/): PyYAML is a Python library for working with YAML (YAML Ain't Markup Language) data. It is commonly used for reading and writing configuration files and data serialization.
- [**APScheduler**](https://apscheduler.readthedocs.io/en/stable/): APScheduler is a Python library that provides advanced scheduling capabilities. In this project, it is used to create a scheduled job for cleaning cached acknowledge messages, allowing for efficient management of data within the application.
- [**Official Telegram bot api**](https://core.telegram.org/bots/api): This project uses just the http api and don't relay on any custom framework to handle messaging with the bot

## Telegram Bot

> Before going to the installation part, you need to create a **telegram bot** and link the token to this backend. Whether you can still run it even without a bot-token, you won't be able to send or receive messages

Check this [Bot Setup Guide](./docs/bot-setup-guide.md) if you are completely new to bots, or if you already know how to do it just open [@BotFather](https://t.me/botfather)

Once you have a telegram bot and bot-token you can create a `.env` file and add this line: 

```env
TELEGRAM_BOT_TOKEN = "<bot_token>"
```
Replace `<bot_token>` with your bot token, **and keep it safe**!

After this step you will need to configure a webhook for your telegram bot in order to let this app handle messages. I used [Postman](https://www.postman.com/) for this part. Just run this api in the postman console: 

The Http method to use is GET
```
https://api.telegram.org/bot<bot_token>/setWebhook?url=<webhook_url>
```
Replace `<bot_token>` with your bot token, and `<webhook_url>` with something like this: 
```
https://<your_url>/bot/webhook_receiver
```
Replace `<your_url>` with the url on which your backend is served.

## Serve the Backend

**Heroku**:
This project uses heroku to serve the backend, unfortunately Heroku isn't free, but offer an affordable basic plan. I decided to use it to speed up the deployment procedures and access an https url without dealing with SSL settings. To check how to configure it check the [Heroku setup guide](./docs/heroku-setup-guide.md).

**Ngrok**: You can also run this app through a ngrok tunnel, it is a tool that proxy a temporary public url to your localhost server. Whether it offers a free plan, it is a good choice just for development reason. Check the [Ngrok setup guide](./docs/ngrok-setup-guide.md) to learn how to use it. 

## Installation

> You'll need `python` installed on your machine before starting this project. To know more about it you can check the official guide linked below

- [Python Official Guide](https://www.python.org/about/gettingstarted/)

To set up the project locally, follow these steps:

- Install virtualenv to handle pyhton virtual environment:

```bash
pip3 install virtualenv
```

- Go to project folder
- Create a virtual environment in which run the BE application

```bash
virtualenv venv --python=python3.11
```
_This command created a `venv` folder inside the root of your project_

- run the virtual environment

```bash
source venv/bin/activate 
```

>to exit the virtual environment just type `deactivate`

>(**_Only in case of error_**):
If for some reason you shouldn't see any venv/bin folder probably you incurred in some cache error. Don't worry tho, you can still access the virtual env by running this command: `source venv/usr/local/bin/activate`
Curious abut this error? check this [github issue](https://github.com/pypa/virtualenv/issues/2319) 

- install requirements
```bash
pip install -r requirements.txt
```

Now the backend is ready to run!

## Usage

To run the backend locally you can use the command below

```bash
flask --debug run 
```

The app will run at http://127.0.0.1:5000 and you should be able to call `/hello` api from [Postman](https://www.postman.com/)

As said earlier i used Heroku to serve the app in order to make it available for the frontend mini app. Check the [Heroku setup guide](./docs/heroku-setup-guide.md).

Or if you just need to serve this backend for development/testing, reasons you can follow the [Ngrok setup guide](./docs/ngrok-setup-guide.md).

### Available Routes
The only available endpoint of this projects are: 
- `/` and `/hello`: used for testing purposes and serve as template guide to add new endpoint to the app
- `/bot/roll_dices`: this api is used by the diceflayer frontend app to send dice rolling requests
- `/bot/webhook_receiver`: this is the webhook endpoint that is called when the bot recieve a message or is added to a group

## Start from zero
You can check this project and use it for reference to create your very own bot as well. Check the code to discover more about the implementations, i added comments and description to simplify the understanding process.
Keep in mind that this is just the **backend** part of the Mini App, **you'll need to check and install also the [frontend](../frontend/README.md)** to have a fully understainding of its logics.

## License

This project is dual-licensed under the **BSD License** and the **MIT License**. You are free to use, modify, and distribute the code. If you fork this project or use it as a base, please remember to cite the original author, [@Tratt0re](https://github.com/Tratt0re), in your documentation.

- [MIT licence](../MIT_LICENSE)
- [BSD licence](../BSD3_LICENSE)

## Full Doc
Full documentations legend available [HERE](./docs/README.md)

