# Develop React Mini App from zero

In this guide, we will walk you through the process of creating a Telegram web app from scratch using Create React App, a popular tool for setting up React applications quickly.

## Prerequisites

Before you begin, make sure you have the following:

- Node.js and npm (Node Package Manager) installed on your computer. You can download them from [nodejs.org](https://nodejs.org/).
- An IDE for writing and editing code (_When in doubt use_ [VS Code](https://code.visualstudio.com/)).
- Basic knowledge of JavaScript, React, and web development concepts.
- A Telegram bot

If you don't know how to create a Telegram bot, you can check the [Telegram Bot setup guide](./bot-setup-guide.md).

## Steps

### 1. Set Up Create React App
- Open your terminal and run the following command to create a new React app using Create React App:

```bash
npx create-react-app <your-app-name>
```
Replace `<your-app-name>` with your desired project name.

- Navigate to your project folder: `cd <your-app-name>`

At this point, you are ready to start developing your app, styling it, and adding some logic. 

If you are new to React you can follow the [React Official Guide](https://react.dev/learn/installation) to learn more and start exploring the development world.


### 2.1 Hosting your app
>To start using your web app as a telegram bot mini app i strongly suggest you to read the official [Telegram Doc](https://core.telegram.org/bots/webapps#initializing-web-apps) first. 

To link your app to a telegram bot you will need to host the application publicly on the internet. 
In this project i'm using **GitHub Pages** to host the production ready application and **Ngrok** when developing new functionalites and styling the app. Learn more about this two powerful tools and how to use them here: 

- [Github Pages setup guide](./gh-pages-setup-guide.md) 
- [Ngrok setup guide](./ngrok-setup-guide.md) 

### 2.2 Linking app to telegram
If you hosted your app and added the public url to the bot menu button, you will probably wandering why it doesn't appear. Most probably is because you didn't read the official doc. as i suggested (😏), but to keep it short you need to add the **Telegram Web App Script** in the head of your web app. 
In order to do that, open the `/public` folder and in the `index.html` add the following script: 

```html
<script src="https://telegram.org/js/telegram-web-app.js?1"></script>
```

**It is very important that this is the first script in the web app `<head>`**

Now commit the changes, push and re-deploy your app. After a couple of minutes you should be able to access the Mini App directly from your bot.

## What's next ?
Now you should be able to access the frontend of the mini app, but you will probably need to adjust it in order to fit your requirements and graphics ideas.

To start interacting with the Telegram components and hooks i suggest you to check this library -> [**react-telegram-web-app**](https://github.com/vkruglikov/react-telegram-web-app).
It is a library that wrap telegram components and utilties in React ready components and hooks. 

You can also acces to this very project to explore its implementation and how it was developed. Remember that this is only the frontend of the telegram mini app, if you are interested on how to manages messages and other technical aspects you should check the backend repo. 

## Are you lost?
Click [HERE](../README.md) to reach the main documentation page.





