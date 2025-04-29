from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from core.security import get_current_user
from core.db import get_db
from sqlalchemy.orm import Session
from services.pdf_reports_service import generate_pdf


pdf_report_router = APIRouter(
    prefix='/pdf',
    tags=['Pdf-Reports']
)


@pdf_report_router.get('/download/{config_id}')
def send_configuration(
    config_id: UUID,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return generate_pdf(config_id, current_user, db)