from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, CheckConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declared_attr, Mapped, mapped_column

BASE = declarative_base()

class Anime(BASE):
    __id__: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    name: Mapped[str] = mapped_column(String)
    season: Mapped[str] = mapped_column(String)
    genres: Mapped[str] = mapped_column(ARRAY(String))
    country: Mapped[str] = mapped_column(String)
    date_of_production: Mapped[str] = mapped_column(Date)
    director: Mapped[str] = mapped_column(String)
    scenario: Mapped[str] = mapped_column(String)
    stuido: Mapped[str] = mapped_column(String)
    age_rating: Mapped[str] = mapped_column(String, 
                        CheckConstraint("age_rating IN ('G', 'PG', 'PG-13', 'R', 'NC-17')"),
                        nullable=False)
    