from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from core.security import get_current_user
from core.db import get_db
from sqlalchemy.orm import Session

from services.assigment_service import send_message_to_ai


assignment_router = APIRouter(
    prefix='/ai',
    tags=['Assignment']
)


@assignment_router.get('/assignment/{config_id}')
def send_configuration(
    config_id: UUID,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return send_message_to_ai(current_user, config_id, db)