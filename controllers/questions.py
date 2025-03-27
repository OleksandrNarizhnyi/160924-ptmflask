from models.questions import Question

from models import db

def get_all_questions() -> list[dict[str,int |str]]:
    questions = Question.query.all()

    questions_data = [
        {
            "id": question.id,
            "text": question.text,
            "category_id": question.category_id
        }
        for question in questions
    ]

    return questions_data

def create_new_question(raw_data: dict[str, str | int]) -> Question:
    new_obj = Question(text=raw_data["text"], category_id=raw_data["category_id"])

    db.session.add(new_obj)
    db.session.commit()

    return new_obj