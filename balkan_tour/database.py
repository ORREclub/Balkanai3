from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database/balkan_bike_tours.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)