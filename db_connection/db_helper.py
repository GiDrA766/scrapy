from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from .settings import settings

class DB_HELPER:
    def __init__(self):
        self.engine = create_engine(settings.url)
        
    def session_maker(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    @contextmanager
    def session(self):
        session = self.session_maker()
        try:
            yield session  # Yielding the session, so it can be used within the 'with' block
        finally:
            session.close()

db_helper = DB_HELPER()
