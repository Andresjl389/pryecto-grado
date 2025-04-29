from fastapi import HTTPException
from models.kitchen_configs import kitchenConfig
from repositories.kitchen_config import delete, get_by, insert_kitchen_config, update
from repositories.kitchen_type import insert_type, get_type_by_id
from schemas.kitchen import CreateKitchenConfig
from sqlalchemy.orm import Session
from uuid import UUID

def create(config: CreateKitchenConfig, current_user: str, db: Session):
    # Obtener ID de tipo de cocina
    if config.kitchen_type:
        # Crear nuevo tipo
        kitchen_type_obj = insert_type(db, config.kitchen_type)
        kitchen_type_id = kitchen_type_obj.id
    else:
        kitchen_type_obj = get_type_by_id(db, config.kitchen_type_id)
        if not kitchen_type_obj:
            raise HTTPException(status_code=404, detail="Kitchen type not found")
        kitchen_type_id = kitchen_type_obj.id

    # Crear la configuración de cocina
    kitchen_config = kitchenConfig(
        name=config.name,
        area=config.area,
        num_stations=config.num_stations,
        staff_count=config.staff_count,
        notes=config.notes,
        user_id=current_user,
        kitchen_type_id=kitchen_type_id,
    )

    return insert_kitchen_config(db, kitchen_config)


def get_by_options(user_id: UUID, kitchen_id: UUID, db: Session):
    return get_by(user_id, kitchen_id, db)

def update_kitchen_config(user_id: UUID, config_id: UUID, config:CreateKitchenConfig, db: Session):
    try:
        config_to_update = get_by(user_id, config_id, db)
        if not config_to_update:
            return HTTPException(status_code=404, detail="La cocina no existe")
        
        for field, value in config.model_dump(exclude_unset=True).items():
            setattr(config_to_update, field, value)


        return update(db, config_to_update)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar el token: {str(e)}")
    
def delete_kitchen_config(user_id: UUID, config_id: UUID, db: Session):
    try:
        config_to_delete = get_by(user_id, config_id, db)
        if not config_to_delete:
            return HTTPException(status_code=404, detail="La cocina no existe")
        
        delete(config_to_delete, db)
        return {'message':'Configuración eliminada correctamente'}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar el token: {str(e)}")