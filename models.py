from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sqlalchemy as sa

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='band')

    def venues(self):
        return [concert.venue for concert in self.concerts]

    @classmethod
    def most_performances(cls, session):
        # Find the band with the most concerts
        return session.query(Band).join(Concert).group_by(Band.id).order_by(sa.func.count(Concert.id).desc()).first()

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

    def play_in_venue(self, session, venue, date):
        new_concert = Concert(band=self, venue=venue, date=date)
        session.add(new_concert)
        session.commit()


class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='venue')

    def bands(self):
        return [concert.band for concert in self.concerts]

    def concert_on(self, session, date):
        return session.query(Concert).filter_by(venue_id=self.id, date=date).first()

    def most_frequent_band(self, session):
        return session.query(Band).join(Concert).filter(Concert.venue_id == self.id).group_by(Band.id).order_by(sa.func.count(Concert.id).desc()).first()


class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
