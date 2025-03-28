from controllers.categories import (
    get_all_categories,
    create_new_category,
    get_category_by_id,
    update_category,
    delete_category
)
from pydantic import ValidationError
from schemas.categories import CategoryBase
from flask import Blueprint, request, jsonify, Response


categories_bp = Blueprint(name='categories', import_name=__name__)

@categories_bp.route('', methods=["GET", "POST"])
def get_categories() -> Response | tuple[Response, int]:
    if request.method == "GET":
        if request.method == "GET":
            categories = get_all_categories()

            return jsonify(categories)

    if request.method == "POST":
        data = request.json

        try:
            new_category = create_new_category(raw_data=data)
        except ValidationError as err:
            return jsonify(err.errors()), 400
        return jsonify(
            CategoryBase(
                id=new_category.id,
                name=new_category.name
            ).model_dump()
        ), 201  # CREATED

@categories_bp.route('<int:id>', methods=["GET", "PUT", "DELETE"])
def retrieve_category(id: int):
    if request.method == "GET":
        category_by_id = get_category_by_id(id=id)

        category_dict = {
            "id": category_by_id.id,
            "name": category_by_id.name
        }
        return jsonify(category_dict)


    if request.method == "PUT":
        category_by_id = get_category_by_id(id=id)
        if not category_by_id:
            return jsonify(
                {
                    "error": f"ID {id} not found."
                }
            ), 404
        data = request.json
        if not data or "name" not in data:
            return jsonify(
                {
                    "error": "No required field provided.('name')"
                }
            ), 400
        updated_category = update_category(obj=category_by_id, new_data=data)
        return jsonify(
            {
                "id": updated_category.id,
                "name": updated_category.name
            }
        ), 200

    if request.method == "DELETE":
        delete_category(id=id)
        return f"CATEGORY BY ID: {id} DELETED"