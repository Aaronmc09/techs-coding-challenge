from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "postgresql+psycopg2://postgres:password@db:5432/records"
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
