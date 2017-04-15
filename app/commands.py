# Functionality of commands will be implemented here so we are able to write
# unit tests without really complicated setups


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
