# This is bootybot
import app.commands as ec
from discord.ext import commands
from app.secrets import TOKEN
from app.settings import PREFIX

bootybot = commands.Bot(command_prefix=PREFIX)


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


@bootybot.command(pass_context=True)
async def meetup(ctx, *, args: str):
    """Creates an event for others to sign up to"""

    await bootybot.say(ec.meetup(ctx, args))


@bootybot.command(pass_context=True)
async def signup(ctx, *, args: str):
    """Sign up for an event"""

    await bootybot.say(ec.signup(ctx, args))


@bootybot.command(pass_context=True)
async def events():
    """Show all events"""

    await bootybot.say(ec.show_meetups())


bootybot.run(TOKEN)
