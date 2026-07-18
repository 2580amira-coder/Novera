from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True
    )

    telegram_id = Column(
        String,
        unique=True,
        nullable=False
    )

    username = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    country = relationship(
        "Country",
        back_populates="owner",
        uselist=False
    )

    def __repr__(self):
        return f"<User {self.username}>"