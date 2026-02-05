from dotenv import load_dotenv
import discord
import os

load_dotenv()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True  #ensure bot can read message 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message) :
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send( 'Hello!')

client.run(os.getenv('TOKEN'))