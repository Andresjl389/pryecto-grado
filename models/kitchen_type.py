import datetime
import uuid
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import relationship
from core.db import Base

class kitchenType(Base):
    __tablename__ = "kitchen_type"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    type = Column(String, index=True, nullable=False)

    kitchen_config = relationship('kitchenConfig', back_populates='kitchen_type')