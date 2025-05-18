import uuid

from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.postgresql import UUID

from app.db import Base


class Message(Base):
    __tablename__ = "messages"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    content = Column(String, nullable=False)
    sentiment = Column(String, nullable=False)
    score_positive = Column(Float, nullable=False)
    score_negative = Column(Float, nullable=False)
    language = Column(String, nullable=False, server_default="pt")
