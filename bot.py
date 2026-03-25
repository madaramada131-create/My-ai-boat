import discord
from discord.ext import commands
from g4f.client import Client
import os

# Token Render ki settings se aayega
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = Client()

@bot.event
async def on_ready():
    print(f'{bot.user} is online and running on Cloud!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if not message.content.startswith('!'):
        async with message.channel.typing():
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message.content}],
                )
                await message.channel.send(response.choices[0].message.content)
            except:
                await message.channel.send("Bhai, server thoda busy hai, dubara try karein.")
    await bot.process_commands(message)

bot.run(TOKEN)
