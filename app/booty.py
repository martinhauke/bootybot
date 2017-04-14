# This is bootybot
import discord
import asyncio
from discord.ext.commands import Bot
from password import TOKEN

bootybot = Bot(command_prefix="!")


@bootybot.event
async def on_read():
    print("Client logged in")


@bootybot.command()
async def hello(*args):
    return await bootybot.say("Hello, World!")


bootybot.run(TOKEN)
