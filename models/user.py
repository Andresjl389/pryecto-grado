import datetime
import uuid
from sqlalchemy import Column, Date, Integer, String, Uuid
from sqlalchemy.orm import relationship
from core.db import Base


from models.kitchen_type import kitchenType
from models.kitchen_configs import kitchenConfig
from models.category import Category
from models.equipment_items import EquipmentItems
from models.assignments import Assignments
from models.recommendations import Recommendations
from models.pdf_reports import PdfReports

class User(Base):
    __tablename__ = "user"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(Date, default=datetime.date.today())

    kitchen_config = relationship('kitchenConfig', back_populates='user')