from db import db
from werkzeug.security import generate_password_hash, check_password_hash

# 사용자 모델 정의
class User(db.Model):
    # 기본 키 및 필드 정의
    id = db.Column(db.Integer, primary_key=True)             # 고유 사용자 ID
    username = db.Column(db.String(50), unique=True, nullable=False)  # 고유 사용자 이름
    password_hash = db.Column(db.String(128))                # 암호화된 비밀번호 저장

    # 비밀번호 설정 메서드
    def set_password(self, password):
        self.password_hash = generate_password_hash(password) # 비밀번호를 해시로 변환하여 저장

    # 비밀번호 검증 메서드
    def check_password(self, password):
        return check_password_hash(self.password_hash, password) # 입력 비밀번호와 해시 비교

# Todo 항목 모델 정의
class Todo(db.Model):
    # 기본 키 및 필드 정의
    id = db.Column(db.Integer, primary_key=True)             # 고유 Todo ID
    title = db.Column(db.String(100), nullable=False)        # Todo 제목
    completed = db.Column(db.Boolean, default=False)         # 완료 여부 (기본값: False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # 연결된 사용자 ID (외래 키)
