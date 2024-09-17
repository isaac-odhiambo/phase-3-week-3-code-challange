from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

# Create an engine
engine = create_engine('sqlite:///concerts.db')

# Create all tables in the engine
Base.metadata.create_all(engine)

# Bind the engine to the session
Session = sessionmaker(bind=engine)
session = Session()

# Sample data
def create_sample_data():
    band1 = Band(name="The Rolling Stones", hometown="London")
    band2 = Band(name="The Beatles", hometown="Liverpool")
    venue1 = Venue(title="Madison Square Garden", city="New York")
    venue2 = Venue(title="Wembley Stadium", city="London")

    session.add_all([band1, band2, venue1, venue2])
    session.commit()

    # Create concerts
    concert1 = Concert(band=band1, venue=venue1, date="2023-09-16")
    concert2 = Concert(band=band1, venue=venue2, date="2023-09-20")
    concert3 = Concert(band=band2, venue=venue1, date="2023-09-18")

    session.add_all([concert1, concert2, concert3])
    session.commit()

def run_queries():
    # Query Band
    band = session.query(Band).first()
    print(f"Band: {band.name}, Hometown: {band.hometown}")
    print(f"Venues: {[venue.title for venue in band.venues()]}")

    # Query Venue
    venue = session.query(Venue).first()
    print(f"Venue: {venue.title}, City: {venue.city}")
    print(f"Bands: {[band.name for band in venue.bands()]}")

    # Query Concert Introduction
    concert = session.query(Concert).first()
    print(concert.introduction())

    # Check Hometown Show
    print(f"Is Hometown Show: {concert.hometown_show()}")

    # Most Frequent Band in a Venue
    print(f"Most Frequent Band at {venue.title}: {venue.most_frequent_band(session).name}")

    # Most Performances by a Band
    print(f"Band with Most Performances: {Band.most_performances(session).name}")


if __name__ == '__main__':
    create_sample_data()
    run_queries()
