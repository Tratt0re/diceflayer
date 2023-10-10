# Ngrok setup guide

[Ngrok](https://ngrok.com/) is a popular tool for exposing local servers to the internet, which can be handy for testing and sharing your app during development. This guide will walk you through the steps to run a Python Flask app on Ngrok.

>***NOTE: You will need to create a ngrok account to use its services. You can use it for free but each time you will run ngrok on your terminal a different url will be provided to you***

## Prerequisites

Before you begin, make sure you have the following:

- A Python app that you want to expose to the internet. (_You can use this one if you want, in this case i suggest you to copy the frontend folder in a new project and start from there._) 
- Ngrok installed on your system. You can download it from [Ngrok's official website](https://ngrok.com/download).

## Steps

### 1. Install Ngrok
If you haven't already installed Ngrok, download and install it following the instructions on the [Ngrok download page](https://ngrok.com/download).

### 2. Start Your Python App

- Open your terminal and navigate to the directory where your python app is located.

- If you are using (as i hope) a virtual environment to run your app in, start it. In this project i used virtualenv to setup a virtual environment, you can start it by running the command `source venv/bin/activate`.

- Start your Flask development server using the command: 

```bash
flask --debug run
```

> If you are using a Mac, as i did, there is a known issue. The port 5000 is the default port Apple uses as Apple AirPlay Receiver. Just set a different port to avoid errors while using ngrok to reverse proxy your local flask address. For e.g. you can use `flask --debug run --port=5050`

This will expose your app on a local development server, typically at `http://127.0.0.1:5000`

> Or (_if you followed my suggestion about mac issues_) on `http://127.0.0.1:5050`

### 3. Expose Your Local Server with Ngrok

- In a new terminal window, navigate to the directory where you have Ngrok installed. (_Or just type ngrok in your terminal if you installed it globally on your system_)

- Use the following command to expose your local Flask app to a public URL: 
``` bash
ngrok http <port>
``` 

**Replace `<port>` with the port your app in running on.**


- Ngrok will provide you with a public URL (e.g., `https://your-subdomain.ngrok.io`) that you can use to access your locally hosted Flask app from anywhere on the internet.

### 4. Link to Telegram Mini App
Now that you are hosting your flask backend app you can add its public url to your frontend app in order to then call your local server from the telegram mini bot interface. In order to do that you can follow the guide i provided in the [Frontend](../../frontend/README.md#installation) part of this project.

## What's next ?
Now you should be able to access the backend of the mini app. 

You can still check how to use [Heroku](./heroku-setup-guide.md) to host the backend for a production environment, or just explore this repo in search of something interesting.

## Are you lost?
Click [HERE](../README.md) to reach the main documentation page.

