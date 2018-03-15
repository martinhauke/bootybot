# Functionality of commands will be implemented here so we are able to write
# unit tests without really complicated setups
from app.models import session, MeetupEvent, MeetupUser
from datetime import datetime
from app.settings import DELIMITER


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
    print("Bla!" + args_str)
    if not args_str:
        print("empty string")
        return show_meetups()

    args_str = args_str.replace("; ", ";")
    print("check:" + args_str)

    user = ctx.message.author
    date, title, event_descr = args_str.split(DELIMITER)

    event_date = datetime.strptime(date, "%d.%m.%Y %H:%M")
    m_event = MeetupEvent(date=event_date,
                          title=title,
                          description=event_descr,
                          created_by=str(user.id))
    session.add(m_event)
    session.commit()

    retstring = "**<@" + user.id + "> created an Event:**" + "\n"
    retstring += "Date: " + m_event.date.strftime("%d.%m.%Y") + "\n"
    retstring += "Time: " + m_event.date.strftime("%H:%M") + "\n"
    retstring += "Title: **" + m_event.title + "**\n"
    retstring += "Description: " + m_event.description + "\n"
    retstring += "--------------" + "\n"
    retstring += "You can sign up for this event by typing *'!signup "
    retstring += str(m_event.id) + "'*."

    return retstring


def signup(ctx, args_str):
    """Sign up for an event."""

    user = ctx.message.author
    args = args_str.split(DELIMITER)
    print(args)
    eid = args[0]
    if (len(args) == 2):
        print("2")
        m_status = args[1]
    else:
        m_status = 1

    db_user = session.query(MeetupUser).filter_by(userid=user.id,
                                                  event_id=eid).first()
    if db_user:
        print("if:" + str(db_user.id))
        m_user = db_user
        m_user.status = m_status
    else:
        m_user = MeetupUser(userid=user.id,
                            event_id=eid,
                            status=m_status)

    m_event = session.query(MeetupEvent).filter_by(id=eid).first()
    if not m_event:
        return "No event found with ID " + eid

    session.add(m_user)
    session.commit()

    retstring = "<@" + user.id + "> signed up for event ["
    retstring += str(m_event.id) + "]: \n"
    retstring += "Status: " + str(m_user.status)

    return retstring


def show_meetups():
    """Show all upcoming events"""

    db_eventlist = session.query(MeetupEvent)

    retstring = "Upcoming events: \n"
    for event in db_eventlist:
        retstring += "[" + str(event.id) + "] **" + event.title
        retstring += "** [" + str(event.date) + "]: \n"
        retstring += event.description + "\n"

    return retstring
