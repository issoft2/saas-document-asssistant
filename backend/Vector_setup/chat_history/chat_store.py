from typing import List, Tuple, Optional
from sqlmodel import Session, select

from Vector_setup.user.db import ChatMessage


def save_chat_turn(
    db: Session,
    tenant_id: str,
    user_id: str,
    user_message: str,
    assistant_message: str,
    conversation_id: Optional[str] = None,
) -> None:
    msgs = [
        ChatMessage(
            tenant_id=tenant_id,
            user_id=user_id,
            role="user",
            content=user_message,
            conversation_id=conversation_id
        ),
        ChatMessage(
            tenant_id=tenant_id,
            user_id=user_id,
            role="assistant",
            content=assistant_message,
            conversation_id=conversation_id,
        ),
    ]
    
    for m in msgs:
        db.add(m)
    db.commit() 
    
def get_last_n_turns(
    db: Session,
    tenant_id: str,
    user_id: str,
    n_turns: int = 3,
    conversation_id: Optional[str] = None,
) -> List[Tuple[str, str]]:
    """
    REturn list of (user_content, assistant_content) for the last_n_turns.
    """
    stmt = (
        select(ChatMessage)
        .where(ChatMessage.tenant_id == tenant_id)
        .where(ChatMessage.user_id == user_id)
        .order_by(ChatMessage.created_at.desc(), ChatMessage.id.desc())
    )
    if conversation_id:
        stmt = stmt.where(ChatMessage.conversation_id == conversation_id)
        
    rows = db.exec(stmt).all()
    # rows are reverse chronological order; group into turns
    turns: List[Tuple[str, str]] = []
    current_user: Optional[str] = None
    current_assistant: Optional[str] = None
    
    for msg in rows:
        if msg.role == "assistant":
            if current_assistant is None:
                current_assistant = msg.content
            elif msg.role == "user":
                if current_user is None:
                    current_user = msg.content
                    
            if current_user is not None and current_assistant is not None:
                turns.append((current_user, current_assistant)) 
                if len(turns) >= n_turns:
                    break
                
                current_user = None
                current_assistant = None
                
    return list(reversed(turns)) # oldest first                                  