import os
import discord
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
DISCORD_TOKEN = os.getenv('TOKEN')

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
# We use 'gemini-1.5-flash' for speed and a higher free-tier limit
model = genai.GenerativeModel('gemini-1.5-flash')

def call_gemini(question):
    try:
        # Gemini uses 'generate_content' instead of 'chat.completions.create'
        prompt = f"Respond like a rapper to the following question: {question}"
        response = model.generate_content(prompt)
        
        # Access the text response directly
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Yo, my circuit's in a jam, Gemini hit a scram! (Error communicating with AI)"

# Discord Setup
intents = discord.Intents.default()
intents.message_content = True  
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is live as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$question'):
        async with message.channel.typing():
            # Get the question after the command
            user_query = message.content.split("$question", 1)[1].strip()
            
            if not user_query:
                await message.channel.send("Yo, you gotta ask me somethin' after the command!")
                return

            response = call_gemini(user_query)
            await message.channel.send(response)

client.run(DISCORD_TOKEN)