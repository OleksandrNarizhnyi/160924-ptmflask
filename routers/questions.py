from flask import Blueprint, request, jsonify, Response
from controllers.questions import (
    get_all_questions,
    create_new_question
)
from models.questions import Question

questions_bp = Blueprint(name="questions", import_name=__name__)


# @questions_bp.route('', methods=["GET"])
# def get_all_questions():
#     return "ALL QUESTIONS"
#
# @questions_bp.route('', methods=["POST"])
# def create_question():
#     return "CREATE QUESTION"
#
#
# @questions_bp.route('/<int:id>', methods=["GET"])
# def get_question_by_id(id: int):
#     return f"QUESTION - {id}"
#
#
# @questions_bp.route('/<int:id>', methods=["PUT"])
# def update_question(id: int):
#     return f"QUESTION UPDATE BY ID - {id}"
#
#
# @questions_bp.route('/<int:id>', methods=["DELETE"])
# def delete_question(id: int):
#     return f"QUESTION DELETE BY ID - {id}"



@questions_bp.route('', methods=["GET", "POST"])
def questions_list() -> Response | tuple[Response, int]:
    if request.method == "GET":
        questions = get_all_questions()

        return jsonify(questions)

    if request.method == "POST":
        data = request.json

        if not data or "text" not in data:
            return jsonify(
                {
                    "error": "No required field provided.('text')"
                }
            ), 400

        new_question = create_new_question(raw_data=data)

        return jsonify(
            {
                "messege": "New question created successfully.",
                "id": new_question.id
            }
        ), 201 #CREATED


@questions_bp.route('/<int:id>', methods=["GET", "PUT", "DELETE"])
def retrieve_question(id: int):
    if request.method == "GET":
        return f"QUESTION - {id}"

    if request.method == "PUT":
        return f"QUESTION UPDATE BY ID - {id}"

    if request.method == "DELETE":
        return f"QUESTION DELETE BY ID - {id}"
