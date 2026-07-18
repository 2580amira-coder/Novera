from datetime import datetime
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from database.database import Base


class Country(Base):
    __tablename__ = "countries"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    flag = Column(
        String,
        default="default.png"
    )

    gold = Column(
        Integer,
        default=5000
    )

    food = Column(
        Integer,
        default=2000
    )

    wood = Column(
        Integer,
        default=1500
    )

    stone = Column(
        Integer,
        default=1500
    )

    iron = Column(
        Integer,
        default=500
    )

    population = Column(
        Integer,
        default=200
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    owner = relationship(
        "User",
        back_populates="country"
    )