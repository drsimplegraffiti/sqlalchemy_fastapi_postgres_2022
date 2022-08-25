from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://postgres:Bassguitar1@localhost/furious1", echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
