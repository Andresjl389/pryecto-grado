from uuid import UUID
from sqlalchemy.orm import Session
from models.kitchen_type import kitchenType
from models.user import User
from schemas.kitchen_type import KitchenTypeBase
from schemas.user_schema import UserCreate
from core.security import get_password_hash


def insert_type(db: Session, type: KitchenTypeBase):
    db_kitche_type = kitchenType(
        type = type.type
        )
    db.add(db_kitche_type)
    db.commit()
    db.refresh(db_kitche_type)
    return db_kitche_type

def get_type_by_type(db: Session, type: str):
    return db.query(kitchenType).filter(kitchenType.type == type).first()

def get_type_by_id(db: Session, id: UUID):
    return db.query(kitchenType).filter(kitchenType.id == id).first()