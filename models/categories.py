from sqlalchemy.orm import Mapped, mapped_column

from models import db

class Category(db.Model):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        db.String(50),
    )

    questions: Mapped[list['Question']] = db.relationship('Question', back_populates='category', cascade="all, delete")

    def __repr__(self):
        return f'Category: {self.name}'