from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.models.models import Message


def delete_old_messages(db: Session):
    threshold = datetime.utc(timezone.now) - timedelta(days=30)
    db.query(Message).filter(Message.created_at < threshold).delete()
    db.commit()
