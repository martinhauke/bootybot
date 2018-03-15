# Testing models.py; This is not really doing anything yet.
# I need to learn more about testing before doing anything clever here.
import unittest
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, MeetupEvent, MeetupUser


class TestModels(unittest.TestCase):

    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()
    mock_ctx = ''

    def setUp(self):
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_insert_meetup_event(self):
        self.session.add(MeetupEvent(
            date=datetime.now() + timedelta(days=1),
            description="This is a Description.",
            created_by="101962887211261952"))
        self.session.commit()

    def test_insert_meetup_user(self):
        self.session.add(MeetupUser(userid="101962887211261952",
                                    event_id=1,
                                    status=0))
        self.session.commit()
