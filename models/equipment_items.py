import datetime
import uuid
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import relationship
from core.db import Base

class EquipmentItems(Base):
    __tablename__ = "equipment_items"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    quantity = Column(Integer, nullable=False)

    kitchen_config_id = Column(Uuid, ForeignKey("kitchen_config.id"))
    category_id = Column(Uuid, ForeignKey("category.id"))

    category = relationship('Category', back_populates='equipment_items')
    kitchen_config = relationship('kitchenConfig', back_populates='equipment_items')