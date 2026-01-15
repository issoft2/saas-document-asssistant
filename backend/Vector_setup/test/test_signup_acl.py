from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session

from Vector_setup.main import app  # your FastAPI app
from Vector_setup.user.db_session import get_db
from Vector_setup.user.db import DBUser, Tenant, Organization
from Vector_setup.user.roles import USER_CREATOR_ROLES
import uuid
import pytest


def _setup_db():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture
def client():
    engine = _setup_db()

    def override_get_db():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


def _create_tenant_and_org(session: Session):
    tenant = Tenant(id="t1", name="Test Tenant")
    session.add(tenant)
    org = Organization(
        id="org-1",
        tenant_id="t1",
        name="Org 1",
        type="subsidiary",
    )
    session.add(org)
    session.commit()
    return tenant, org


def _create_creator(session: Session, role: str):
    user = DBUser(
        id=str(uuid.uuid4()),
        email=f"{role}@example.com",
        tenant_id="t1",
        organization_id="org-1",
        hashed_password="x",
        first_name="Admin",
        last_name="User",
        date_of_birth="2000-01-01",
        phone="123",
        role=role,
    )
    session.add(user)
    session.commit()
    return user


def test_employee_cannot_signup_user(client: TestClient):
    # arrange
    with next(get_db()) as db:
        tenant, org = _create_tenant_and_org(db)
        creator = _create_creator(db, role="employee")

    token = "..."  # stub your auth layer or mock decode_and_get_user

    resp = client.post(
        "/signup",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "email": "new@ex.com",
            "password": "secret",
            "first_name": "New",
            "last_name": "User",
            "tenant_id": "t1",
            "organization_id": "org-1",
            "role": "employee",
        },
    )
    assert resp.status_code == 403
