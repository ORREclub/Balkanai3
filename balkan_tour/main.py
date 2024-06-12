from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Tour, Client, Bike, Booking  #situ gal ir  nereikia nes vistiek yra Base


# čia sukuriu SQLAlchemy variklį
engine = create_engine('sqlite:///database/balkan_bike_tours.db')
Session = sessionmaker(bind=engine) #cia engine sukabinu su session,sukuriu sesijos gamintoja
session=Session() #sukuriu sesija
# susikuriu lenteles kurias pasiimu iš Base models.py
Base.metadata.create_all(engine)


# čia  tik tikrinuos ar įkrauna į duombazę tura
# session = Session()
# new_tour = Tour(name="Balkan Tour", description="Discover the beauty of the Balkans", location="Balkans")
# session.add(new_tour)
# session.commit()
# session.close()

# Prisidedu nauja dvirati pasitikrint
# new_bike = Bike(brand='Trek', model='X500', type='Mountain')
# session.add(new_bike)
# session.commit()
# session.close()