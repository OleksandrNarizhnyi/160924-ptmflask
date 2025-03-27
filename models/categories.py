from sqlalchemy.orm import Mapped, mapped_column

from models import db

class Category(db.Model):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        db.Integer,
        db.Identity(always=True),
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        db.String(50),
        nullable=True
    )

    question: Mapped['Question'] = db.relationship('Question', back_populates='categories', cascade="all, delete")

    def __repr__(self):
        return f'Category: {self.name}'