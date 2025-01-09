from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import create_access_token
from models import User
from werkzeug.security import check_password_hash

# 인증 관련 Blueprint 생성
auth_blp = Blueprint(
    'auth', 'auth', 
    url_prefix='/login', 
    description='Operations on authentication'
)

# 로그인 엔드포인트 정의
@auth_blp.route('/', methods=['POST'])
def login():
    # 요청이 JSON 형식인지 확인
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    # 사용자명과 비밀번호 가져오기
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # 사용자명 또는 비밀번호 누락 확인
    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    # 데이터베이스에서 사용자 검색
    user = User.query.filter_by(username=username).first()

    # 사용자 존재 여부와 비밀번호 확인
    if user and check_password_hash(user.password_hash, password):
        # JWT 토큰 생성
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)  # 토큰 반환
    else:
        # 인증 실패 시 메시지 반환
        return jsonify({"msg": "Bad username or password"}), 401
