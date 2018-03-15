# Database models
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint


# Set stuff up
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///dev_db.sqlite')
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()


class MeetupEvent(Base):
    __tablename__ = 'meetup_event'
    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime, default=func.now())
    created_by = Column(String)
    date = Column(DateTime, CheckConstraint("date > date()",  # date() is sqlite specific
                                            name="checkDateIsFuture"))
    title = Column(String)
    description = Column(String)


class MeetupUser(Base):
    __tablename__ = 'meetup_user'
    id = Column(Integer, primary_key=True)
    userid = Column(String)
    event_id = Column(Integer, ForeignKey('meetup_event.id'))
    status = Column(Integer)  # TODO: add contraints? [1,3]

    meetup_event = relationship(
        MeetupEvent,
        backref=backref('meetup_event',
                        uselist=True,
                        cascade='delete,all'))

Base.metadata.create_all(engine)
