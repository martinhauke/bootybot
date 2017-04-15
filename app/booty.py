# This is bootybot
import discord
import asyncio
import commands as ec
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


@bootybot.event
async def on_message(message):
    """Does not do anything except forwarding input to commands, yet"""
    ec.print_message(message)
    await bootybot.process_commands(message)


@bootybot.command()
async def hello(*args):
    """Replies with 'Hello, World!'."""
    await bootybot.say(ec.hello(args))


@bootybot.command()
async def echo(*, message: str):
    """Repeats the user's input."""
    await bootybot.say(ec.echo(message))


@bootybot.command()
async def ping():
    """Returns 'pong!'
 
    Can be used to check the connection."""
    await bootybot.say(ec.ping())


bootybot.run(TOKEN)
