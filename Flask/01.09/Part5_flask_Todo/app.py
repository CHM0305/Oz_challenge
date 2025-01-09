from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from db import db
from flask_migrate import Migrate

# Flask 앱 생성
app = Flask(__name__)

# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # SQLite 데이터베이스 경로 설정
app.config['JWT_SECRET_KEY'] = 'super-secret-key'           # JWT 인증에 사용할 비밀 키 설정
app.config['API_TITLE'] = 'Todo API'                       # API 문서의 제목
app.config['API_VERSION'] = 'v1'                           # API 버전
app.config['OPENAPI_VERSION'] = '3.0.2'                    # OpenAPI 문서 버전

# 데이터베이스 초기화 및 마이그레이션 설정
db.init_app(app)
migrate = Migrate(app, db)

# JWT 및 API 관리 설정
jwt = JWTManager(app)
api = Api(app)

# 모델과 라우트 불러오기
from models import User, Todo               # 사용자와 Todo 모델 정의 파일
from routes.auth import auth_blp            # 인증 라우트 Blueprint
from routes.todo import todo_blp            #  라우트 Blueprint

# API에 Blueprint 등록
api.register_blueprint(auth_blp)            # 인증 관련 라우트 등록
api.register_blueprint(todo_blp)            #  관련 라우트 등록

# 기본 페이지 렌더링
@app.route("/")
def index():
    return render_template('index.html')    # index.html 페이지 렌더링

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)                     # 디버그 모드로 애플리케이션 실행
