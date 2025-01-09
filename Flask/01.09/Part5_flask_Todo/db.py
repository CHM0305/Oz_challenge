from db import db
from app import app
from models import User

with app.app_context():
    # 새 사용자 생성
    new_user = User(username='newuser')
    new_user.set_password('user123')  # 비밀번호를 해시화하는 메서드 호출
    db.session.add(new_user)
    db.session.commit()
    
    # 사용자 확인
    user = User.query.filter_by(username='newuser').first()
    print(user)