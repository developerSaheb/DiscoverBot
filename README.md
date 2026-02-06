# Discover, The Discord Bot
**DiscoverBot** is a fun Discord bot that answers questions... like a rapper! 🎤 


This project demonstrates how to build a Discord agent using Python, with options to power it via **OpenAI** or **Google Gemini**.

## ✨ Features
* **$hello**: A simple command to check if the bot is alive.
* **$question [text]**: The bot takes a question and responds with a freestyle rap answer.
* **Dual AI Support**: Includes scripts for both OpenAI (GPT-4o) and Google Gemini (Flash).

## .env File
Add the .env file and add discord bot token and key from OpenAI and Gemini 

Token for the discord bot: https://discord.com/developers/applications 

OpenAI key: https://platform.openai.com/account/api-keys 

Gemini key: https://aistudio.google.com/app/u/4/api-keys


# Rapper bot with Gemini
following commands will run the rapper bot with Gemini 

pip install -r requirements.txt 

python discover_bot_with_gemini.py


# Rapper bot with OpenAI
following commands will run the rapper bot with OpenAI 

pip install -r requirements.txt 

python discover_bot_with_openai.py
