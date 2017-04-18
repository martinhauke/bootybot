# Functionality of commands will be implemented here so we are able to write
# unit tests without really complicated setups
from models import session


def hello(args=None):
    """Prints 'Hello, World!'"""
    return "Hello, World!"


def echo(msg):
    """Returns the Input"""
    return msg


def print_message(msg):
    """Prints a message"""
    print(message_to_string(msg))


def message_to_string(msg):
    """Converts a message to String."""
    msg_time = msg.timestamp.strftime('%Y-%m-%d %H:%M:S')
    msg_string = "[ " + msg_time + " ]: "
    msg_string += msg.content

    return msg_string.encode('utf-8')


def list(*args):
    """Manages lists"""
    pass


def ping():
    """Returns 'pong!'"""
    return "pong!"


def meetup(args_str):
    """Creates an event for people to sign up to.

    At least that is the plan."""
    print(args_str)
    # Get the arguments

    # Write to database
    return 'Not yet implemented'
