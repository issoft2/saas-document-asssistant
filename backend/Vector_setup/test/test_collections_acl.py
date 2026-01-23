import uuid
from sqlmodel import Session

from Vector_setup.user.db import DBUser, Collection, Tenant
from Vector_setup.access.collections_acl import user_can_access_collection
from Vector_setup.user.db import CollectionVisibility


def _mk_tenant(db: Session, tenant_id: str = "t1") -> Tenant:
    t = Tenant(id=tenant_id, name="Test Tenant")
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


def _mk_user(db: Session, tenant_id: str, role: str, org_id: str | None = None) -> DBUser:
    u = DBUser(
        id=str(uuid.uuid4()),
        email=f"{role}@example.com",
        tenant_id=tenant_id,
        organization_id=org_id,
        hashed_password="x",
        first_name="Test",
        last_name="User",
        date_of_birth="2000-01-01",
        phone="123",
        role=role,
    )
    db.add(u)
    db.commit()
    db.refresh(u)
    return u


def _mk_collection(
    db: Session,
    tenant_id: str,
    name: str,
    visibility: CollectionVisibility,
    org_id: str | None = None,
    allowed_roles: list[str] | None = None,
    allowed_user_ids: list[str] | None = None,
) -> Collection:
    c = Collection(
        id=str(uuid.uuid4()),
        tenant_id=tenant_id,
        organization_id=org_id,
        name=name,
        visibility=visibility,
        allowed_roles=allowed_roles,
        allowed_user_ids=allowed_user_ids,
    )
    db.add(c)
    db.commit()
    db.refresh(c)
    return c


def test_tenant_visibility_allows_sub_user(db: Session):
    tenant = _mk_tenant(db)
    user = _mk_user(db, tenant.id, role="employee")
    coll = _mk_collection(db, tenant.id, "policies", CollectionVisibility.tenant)

    assert user_can_access_collection(user, coll) is True


def test_org_visibility_requires_same_org(db: Session):
    tenant = _mk_tenant(db)
    org_a = "org-a"
    org_b = "org-b"

    user_a = _mk_user(db, tenant.id, role="sub_hr", org_id=org_a)
    user_b = _mk_user(db, tenant.id, role="sub_hr", org_id=org_b)

    coll = _mk_collection(
        db,
        tenant.id,
        "policies_org",
        CollectionVisibility.org,
        org_id=org_a,
    )

    assert user_can_access_collection(user_a, coll) is True
    assert user_can_access_collection(user_b, coll) is False


def test_role_visibility_requires_role_and_org_match(db: Session):
    tenant = _mk_tenant(db)
    org = "org-a"

    user_hr = _mk_user(db, tenant.id, role="sub_hr", org_id=org)
    user_emp = _mk_user(db, tenant.id, role="employee", org_id=org)

    coll = _mk_collection(
        db,
        tenant.id,
        "hr_only",
        CollectionVisibility.role,
        org_id=org,
        allowed_roles=["sub_hr"],
    )

    assert user_can_access_collection(user_hr, coll) is True
    assert user_can_access_collection(user_emp, coll) is False


def test_user_visibility_requires_explicit_user(db: Session):
    tenant = _mk_tenant(db)
    user1 = _mk_user(db, tenant.id, role="employee")
    user2 = _mk_user(db, tenant.id, role="employee")

    coll = _mk_collection(
        db,
        tenant.id,
        "personal",
        CollectionVisibility.user,
        allowed_user_ids=[user1.id],
    )

    assert user_can_access_collection(user1, coll) is True
    assert user_can_access_collection(user2, coll) is False


def test_group_role_can_access_any_tenant_collection(db: Session):
    tenant = _mk_tenant(db)
    group_admin = _mk_user(db, tenant.id, role="group_admin")

    coll = _mk_collection(
        db,
        tenant.id,
        "any",
        CollectionVisibility.org,
        org_id="org-x",
    )

    assert user_can_access_collection(group_admin, coll) is True
