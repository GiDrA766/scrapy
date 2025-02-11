from sqlalchemy import create_engine
from settings import settings
from sqlalchemy.orm import sessionmaker


class DB_HELPER:
    def __init__(self):
        self.engine = create_engine(settings.url)
        
    def session_maker(self):
        Session = sessionmaker(bind=self.engine)
        return Session()
    def session(self):
        with self.session_maker() as session:
            yield session
            session.close()
            

db_helper = DB_HELPER()