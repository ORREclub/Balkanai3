from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_models_module import Tour  # Import your Tour model

# Create an engine
engine = create_engine('sqlite:///C:/Users/Fujitsu/PycharmProjects/Balkanai/balkan_tour/database/balkan_bike_tours.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a new tour
new_tour = Tour(
    name='Makedonia',
    description='YBla bla',
    location='spain',
    date_start=datetime(2024, 5, 1),  # Example start date
    date_end=datetime(2024, 5, 7)      # Example end date
)

# Add the new tour to the session
session.add(new_tour)

# Commit the session to save changes to the database
session.commit()

# Close the session
session.close()