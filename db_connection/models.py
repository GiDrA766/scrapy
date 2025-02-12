from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, CheckConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declared_attr, Mapped, mapped_column

Base = declarative_base()

class Anime(Base):
    __tablename__ = "anime"  # Explicit table name for clarity

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    name: Mapped[str] = mapped_column(String, nullable=False)
    season: Mapped[str] = mapped_column(String, nullable=True)
    year: Mapped[int] = mapped_column(Integer, nullable=True)
    
    # Use ARRAY(String) for PostgreSQL, or JSON for broader compatibility
    genres: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=True)  
    
    country: Mapped[str] = mapped_column(String, nullable=True)
    date_of_production: Mapped[Date] = mapped_column(Date, nullable=True)  # Changed from DateTime to Date
    
    director: Mapped[str] = mapped_column(String, nullable=True)
    scenario: Mapped[str] = mapped_column(String, nullable=True)
    studio: Mapped[str] = mapped_column(String, nullable=True)  # Fixed "stuido" typo
    
    age_rating: Mapped[str] = mapped_column(
        String,
        CheckConstraint("age_rating IN ('G', 'PG', 'PG-13', 'R', 'NC-17')"),
        nullable=False,
        server_default="PG"  # Default value to avoid NULL issues
    )
