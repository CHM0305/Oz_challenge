from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Todo, User, db

#  관련 Blueprint 생성
todo_blp = Blueprint(
    'todo', 'todo', 
    url_prefix='/todo', 
    description='Operations on todos'
)

#  생성 (POST)
@todo_blp.route('/', methods=['POST'])
@jwt_required()  # JWT 인증 요구
def create_todo():
    # 요청이 JSON 형식인지 확인
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    # 제목 가져오기
    title = request.json.get('title', None)
    if not title:
        return jsonify({"msg": "Missing title"}), 400

    # 현재 로그인한 사용자 가져오기
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()

    # 새 Todo 항목 생성
    new_todo = Todo(title=title, user_id=user.id)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"msg": "Todo created", "id": new_todo.id}), 201

#  조회 (GET)
@todo_blp.route('/', methods=['GET'])
@jwt_required()  # JWT 인증 요구
def get_todos():
    # 현재 로그인한 사용자 가져오기
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()

    # 사용자 ID와 연결된 Todo 항목 가져오기
    todos = Todo.query.filter_by(user_id=user.id).all()
    return jsonify([
        {"id": todo.id, "title": todo.title, "completed": todo.completed}
        for todo in todos
    ])

#  수정 (PUT)
@todo_blp.route('/<int:todo_id>', methods=['PUT'])
@jwt_required()  # JWT 인증 요구
def update_todo(todo_id):
    #  항목 가져오기
    todo = Todo.query.get_or_404(todo_id)

    # 요청 JSON에 따라 제목 및 완료 상태 업데이트
    if 'title' in request.json:
        todo.title = request.json['title']
    if 'completed' in request.json:
        todo.completed = request.json['completed']

    db.session.commit()  # 데이터베이스에 변경 사항 저장
    return jsonify({"msg": "Todo updated", "id": todo.id})

#  삭제 (DELETE)
@todo_blp.route('/<int:todo_id>', methods=['DELETE'])
@jwt_required()  # JWT 인증 요구
def delete_todo(todo_id):
    #  항목 가져오기
    todo = Todo.query.get_or_404(todo_id)

    #  항목 삭제
    db.session.delete(todo)
    db.session.commit()

    return jsonify({"msg": "Todo deleted", "id": todo_id})
