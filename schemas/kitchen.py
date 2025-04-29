from typing import Optional
from pydantic import BaseModel, UUID4, model_validator
from datetime import datetime

from schemas.kitchen_type import GetKitchenType, KitchenTypeBase


class CreateKitchenConfig(BaseModel):
    name: str
    area: float
    num_stations: int
    staff_count: int
    notes: str
    kitchen_type_id: Optional[UUID4] = None 
    kitchen_type: Optional[KitchenTypeBase] = None

    @model_validator(mode='after')
    def validate_kitchen_type(self):
        if not self.kitchen_type_id and not self.kitchen_type:
            raise ValueError("You must provide either kitchen_type_id or kitchen_type")
        if self.kitchen_type_id and self.kitchen_type:
            raise ValueError("Provide only one: either kitchen_type_id or kitchen_type")
        return self
    


class KitchenConfigBase(BaseModel):
    id: UUID4
    user_id: UUID4
    kitchen_type_id: UUID4
    created_at: datetime
    name: str
    area: float
    num_stations: int
    staff_count: int
    notes: str