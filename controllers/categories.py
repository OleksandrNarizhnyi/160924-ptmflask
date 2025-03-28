from models.categories import Category
from schemas.categories import CategoryBase
from models import db


def get_all_categories() -> list[dict[str,int |str]]:
    categories = Category.query.all()

    categories_data = [
        {
            "id": category.id,
            "name": category.name,
        }
        for category in categories
    ]

    return categories_data

def create_new_category(raw_data: dict[str, str]):
    validated_obj = CategoryBase.model_validate(raw_data)

    new_obj = Category(name=validated_obj.name)

    db.session.add(new_obj)
    db.session.commit()

    return new_obj


def get_category_by_id(id: int) -> dict[str, int | str]:
    category_by_id = Category.query.get_or_404(id)

    return category_by_id


def update_category(obj, new_data):
    obj.name = new_data["name"]
    db.session.commit()
    return obj

def delete_category(id):
    category = Category.query.get(id)
    if category:
        # Удаляем категорию
        db.session.delete(category)
        db.session.commit()
        return f"Category {id} was deleted"
    else:
        return f"Category {id} not found", 404
