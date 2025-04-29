from pydantic import BaseModel, UUID4
from datetime import datetime

class GetKitchenType(BaseModel):
    id: UUID4
    type: str

class KitchenTypeBase(BaseModel):
    type: str

    
    