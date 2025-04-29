from fastapi import APIRouter, Depends
from uuid import UUID
from core.security import get_current_user
from schemas.kitchen import CreateKitchenConfig, KitchenConfigBase
from core.db import get_db
from sqlalchemy.orm import Session
from services.kitchen_service import create, delete_kitchen_config, get_by_options, update_kitchen_config


kitchen_router = APIRouter(
    prefix='/kitchen',
    tags=['kitchen']
)

@kitchen_router.post('/config', response_model=KitchenConfigBase)
def create_config(
    kitchen: CreateKitchenConfig,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create(kitchen, current_user, db)


@kitchen_router.get('/config/{config_id}', response_model=KitchenConfigBase)
def get_by(
    config_id: UUID,
    current_user: str =Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_by_options(current_user, config_id, db)


@kitchen_router.put('/config/{config_id}')
def update_config(
    config_id: UUID,
    config: CreateKitchenConfig,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_kitchen_config(current_user,config_id, config, db)

@kitchen_router.delete('/config/{config_id}')
def delete_config(
    config_id: UUID,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return delete_kitchen_config(current_user, config_id, db)