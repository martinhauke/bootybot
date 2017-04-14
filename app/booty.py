# This is bootybot
import discord
import asyncio
from discord.ext import commands
from secrets import TOKEN

bootybot = commands.Bot(command_prefix="!")
print(TOKEN)


@bootybot.event
async def on_ready():
    print("Client logged in")


@bootybot.command()
async def hello(*args):
    return await bootybot.say("Hello, World!")


bootybot.run(TOKEN)
