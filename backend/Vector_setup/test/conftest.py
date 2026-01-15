import uuid
import pytest
from sqlmodel import SQLModel, create_engine, Session

from Vector_setup.user.db import DBUser, Collection, Organization, Tenant


@pytest.fixture
def engine():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture
def db(engine):
    with Session(engine) as session:
        yield session
