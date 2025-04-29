import datetime
import uuid
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import relationship
from core.db import Base

class Assignments(Base):
    __tablename__ = "assignments"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    distribution = Column(String, index=True, nullable=False)
    created_at = Column(Date, default=datetime.date.today())

    kitchen_config_id = Column(Uuid, ForeignKey("kitchen_config.id"))

    kitchen_config = relationship('kitchenConfig', back_populates='assignments')