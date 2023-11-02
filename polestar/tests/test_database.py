import pytest
from sqlalchemy import create_engine, Column, String, Integer, Delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from polestar.services.ships import get_all_ships
from polestar.services.positions import get_ship_position
from polestar.models import models
from datetime import datetime
import uuid
from sqlalchemy_utils import create_database, database_exists

Base = declarative_base()


@pytest.fixture
def postgresql_engine(pytestconfig):
    # Set up the PostgreSQL engine for the test database
    engine = create_engine("postgresql://postgres:password@localhost:5433/test_databasenew")
    if not database_exists(engine.url):
        create_database(engine.url)
    models.metadata.create_all(engine)
    return engine


@pytest.fixture
def db_session(postgresql_engine):
    # Create a database session for the test
    Session = sessionmaker(bind=postgresql_engine)
    session = Session()
    yield session
    session.close()


def test_get_all_ships(postgresql_engine, db_session):
    db_session.execute(models.ships.delete())
    expected_ships = [
        {"IMO_number": 12546, "ship_name": "Ship1", "create_ts": datetime.utcnow(), "update_ts": datetime.utcnow()},
        {"IMO_number": 79012, "ship_name": "Ship2", "create_ts": datetime.utcnow(), "update_ts": datetime.utcnow()},
    ]

    db_session.execute(models.ships.insert().values(expected_ships))
    db_session.commit()
    result = get_all_ships(db_session)
    assert len(result) == len(expected_ships)


def test_get_ship_position(postgresql_engine, db_session):
    # Example test case for get_ship_position function
    db_session.execute(models.locations.delete())
    db_session.execute(models.ships.delete())

    expected_ships = [
        {"IMO_number": 123456, "ship_name": "Ship1", "create_ts": datetime.utcnow(), "update_ts": datetime.utcnow()},
        {"IMO_number": 567891, "ship_name": "Ship2", "create_ts": datetime.utcnow(), "update_ts": datetime.utcnow()},
    ]
    db_session.execute(models.ships.insert().values(expected_ships))

    sample_data = [
        {"id":uuid.uuid4(), "IMO_number": 123456, "timestamp": "2023-01-01 12:00:00", "latitude": 10.0, "longitude": 20.0},
        {"id":uuid.uuid4(), "IMO_number": 123456, "timestamp": "2023-01-01 13:00:00", "latitude": 11.0, "longitude": 21.0},
        {"id":uuid.uuid4(), "IMO_number": 567891, "timestamp": "2023-01-01 13:00:00", "latitude": 11.0, "longitude": 21.0},
        {"id":uuid.uuid4(), "IMO_number": 567891, "timestamp": "2023-01-01 13:00:00", "latitude": 11.0, "longitude": 21.0},
    ]

    db_session.execute(models.locations.insert().values(sample_data))
    db_session.commit()
    imo_number = 123456
    result = get_ship_position(db_session, imo_number)
    assert result is not None
    assert len(result) == 2
