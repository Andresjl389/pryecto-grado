from uuid import UUID
from sqlalchemy.orm import Session
from models.kitchen_configs import kitchenConfig
from schemas.kitchen import KitchenConfigBase


def insert_kitchen_config(db: Session, kitchen_config: kitchenConfig) -> KitchenConfigBase:
    db.add(kitchen_config)
    db.commit()
    db.refresh(kitchen_config)
    return kitchen_config


def get_by(user_id: UUID, kitchen_id: UUID, db: Session):
    return db.query(kitchenConfig).filter(
        kitchenConfig.user_id == user_id,
        kitchenConfig.id == kitchen_id
    ).first()



def update(db: Session, config: kitchenConfig):
    db.commit()
    db.refresh(config)
    return config

def delete(config: kitchenConfig, db: Session):
    db.delete(config)
    db.commit()
    return config