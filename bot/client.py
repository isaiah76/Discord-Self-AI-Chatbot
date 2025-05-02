"""
Discord client setup
"""
import discord
from discord.ext import commands
from bot.events import on_ready as handle_ready, on_message as handle_message

# Initialize Discord client
client = commands.Bot(command_prefix="1", self_bot=True)

@client.event
async def on_ready():
    await handle_ready(client)

@client.event
async def on_message(message):
    await handle_message(client, message)
