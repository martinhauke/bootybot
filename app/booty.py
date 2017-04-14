# This is bootybot
import discord
import asyncio
from discord.ext import commands
from secrets import TOKEN

bootybot = commands.Bot(command_prefix="!")


@bootybot.event
async def on_ready():
    print("[STATUS]")
    print("Client logged")
    print(bootybot.user.name)
    print(bootybot.user.id)
    print('--------')


@bootybot.command()
async def hello(*args):
    """Replies with 'Hello, World!'."""
    await bootybot.say("Hello, World!")


bootybot.run(TOKEN)
