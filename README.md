# phase-3-week-3-code-challange
# Models and Relationships:
# Band:

Attributes: name, hometown
Relationships: A Band has many Concerts.
# Venue:

Attributes: title, city
Relationships: A Venue has many Concerts.
# Concert:

Attributes: date, time, etc. (optional fields for additional data)
Relationships: A Concert belongs to one Band and one Venue.
The Concert is the join model between Band and Venue, holding foreign keys that reference both.


# Key Concepts:
Single Source of Truth: The Concert model is the intermediary table that manages the relationship between Band and Venue. It holds the foreign keys for both, making it the "single source of truth" for determining which band plays at which venue and when.
# Steps to Approach:
Draw a UML diagram or relationship chart. For example:
Band → concerts ← Concert → venue ← Venue
Write SQLAlchemy models, like shown above.
Migrations: Use tools like Flask-Migrate or Alembic to manage database changes.
Seeding Data: Ensure you seed both Band, Venue, and the many-to-many Concert data.
This setup allows querying which bands played in specific venues, as well as finding out where and when a particular band performed.


# step in bulding this concert domain 
# Step 1: Project Setup
Before you begin, make sure you have the necessary Python packages installed:
# Step 2: Migrations
We'll first create the migrations for the bands, venues, and concerts tables.

Alembic Migration:

Migration File (located in versions/ folder, named something like create_concert_schema.py):

