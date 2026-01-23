import uuid
from typing import Optional, Dict, Any
from sqlmodel import Session

from Vector_setup.user.db import AuditLog, DBUser


def write_audit_log(
    db: Session,
    user: DBUser,
    action: str,
    resource_type: str,
    resource_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> None:
    log = AuditLog(
        id=str(uuid.uuid4()),
        tenant_id=user.tenant_id,
        user_id=user.id,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        metadata=metadata or {},
    )
    db.add(log)
    db.commit()
