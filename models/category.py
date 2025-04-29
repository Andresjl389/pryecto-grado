import datetime
import uuid
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import relationship
from core.db import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)

    equipment_items = relationship('EquipmentItems', back_populates='category')