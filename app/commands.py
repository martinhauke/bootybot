# Functionality of commands will be implemented here so we are able to write
# unit tests without really complicated setups
from app.models import session, MeetupEvent
from datetime import datetime


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


def meetup(ctx, args_str):
    """Creates an event for people to sign up to.

    At least that is the plan."""
    user = ctx.message.author
    date, event_descr = args_str.split(";")

    event_date = datetime.strptime(date, "%d.%m.%Y %H:%M")
    m_event = MeetupEvent(date=event_date,
                          description=event_descr,
                          created_by=str(user.id))
    session.add(m_event)
    session.commit()

    retstring = "**<@" + user.id + "> created an Event:**" + "\n"
    retstring += "Date: " + m_event.date.strftime("%d.%m.%Y") + "\n"
    retstring += "Time: " + m_event.date.strftime("%H:%M") + "\n"
    retstring += "Description: " + m_event.description + "\n"
    retstring += "--------------" + "\n"
    retstring += "You can sign up for this event by typing '!signup "
    retstring += str(m_event.id) + "'."

    return retstring
