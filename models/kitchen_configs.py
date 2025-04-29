import datetime
import uuid
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import relationship
from core.db import Base

class kitchenConfig(Base):
    __tablename__ = "kitchen_config"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    area = Column(Float, nullable=False)
    num_stations = Column(Integer, nullable=False)
    staff_count = Column(Integer, nullable=False)
    notes = Column(String, index=True, nullable=False)
    created_at = Column(Date, default=datetime.date.today())

    kitchen_type_id = Column(Uuid, ForeignKey("kitchen_type.id"))
    user_id = Column(Uuid, ForeignKey("user.id"))

    user = relationship('User', back_populates='kitchen_config')
    kitchen_type = relationship('kitchenType', back_populates='kitchen_config')
    equipment_items = relationship('EquipmentItems', back_populates='kitchen_config')
    assignments = relationship('Assignments', back_populates='kitchen_config')
    recommendations = relationship('Recommendations', back_populates='kitchen_config')
    pdf_reports = relationship('PdfReports', back_populates='kitchen_config')