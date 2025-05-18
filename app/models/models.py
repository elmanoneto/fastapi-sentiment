import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Float, String
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
    created_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
