# Creating a Telegram Bot using BotFather

BotFather is a special Telegram bot that allows you to create and manage your own Telegram bots. Follow these steps to create your own Telegram bot:

## Prerequisites

Before you begin, you'll need:

- A Telegram account.
- The Telegram app installed on your mobile device or desktop.

## Steps

1. **Open Telegram:** Open the Telegram app on your mobile device or desktop.

2. **Search for BotFather:** In the Telegram search bar, type `@BotFather` and select the official BotFather account.

3. **Start a Chat:** Start a chat with BotFather by clicking on the "Start" button.

4. **Create a New Bot:** Type the following command to create a new bot: `/newbot`

5. **Name Your Bot:** BotFather will ask you to choose a name for your bot. This name will be displayed in chat lists, and users can search for your bot using this name. Enter the desired name for your bot.

6. **Choose a Username:** After selecting a name, BotFather will ask you to choose a username for your bot. The username must be unique and end with the word "bot" (e.g., `mydicerollingbot`). If your chosen username is available, BotFather will confirm it.

>Note: The username is the unique identifier for your bot, and it should be memorable and easy to type.

7. **Bot Created:** BotFather will provide you with a message confirming that your bot has been created, along with an API token. The API token is essential for interacting with your bot programmatically.

>**Keep your API token secure, as it allows access to your bot's functionality and data. Do not share it with others or commit it to public repositories.**

8. **Customize Your Bot:** You can further customize your bot by adding a description, profile picture, and other settings using BotFather's commands.

## Using Your Telegram Bot

Now that you've created your Telegram bot, you can start using it in your chats and channels. You can interact with your bot by sending messages to it or by adding it to groups and channels.

To access your bot's functionality programmatically, you'll need to use the API token provided by BotFather. You can use this token to make API requests to the Telegram Bot API and automate interactions with your bot.

Congratulations! You've successfully created your own Telegram bot using BotFather.

## Link the backend to the Bot
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

## What's next ?
Now that you have a bot you can follow the steps to [serve the backend app](../README.md#serve-the-backend) or run it locally.

## Are you lost?
Click [HERE](../README.md) to reach the main documentation page.