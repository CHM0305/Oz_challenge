from flask import Flask
from flask_mysqldb import MySQL
import yaml 
from flask_smorest import Api
from posts_routes import create_posts_blueprint

#pip install 해줘야한다.
# 만들어 놓은 posts_rotues 파일을 호출
# 블루프린트란 어플리케이션 컴포넌트를 만들고 공통 패턴을 지워하기 위해 사용하는 개념으로 여러번 등록이 가능함.


app = Flask(__name__)
# 플라스크 애플리케이션을 생성하는 코드로 __name__는 파일이 실행될 때 실행되는 모듈이 담기는 변수
# Flask 웹 애플리케이션을 만드는 데 사용되는 핵심 클래스, (라우트처리, 요청 및 응답 처리, 템플릿 렌더링 같은 기능있음.)
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

# bluepring 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app) 
# Api(Application Programming Interface)-애플리케이션 소프트웨어 간에 데이터, 기능, 특징을 
# 교환할 수 있도록 하는 규칙이나 프로토콜의 기능을 하며 컴퓨터 프러그램 간의 연결 역할을 함.
post_blp = create_posts_blueprint(mysql)
#플라스크에서 애플리케이션 객체에 블루프린트를 등록하는 함수!
api.register_blueprint(posts_blp)

# 실행 구간 (변수값이 맞는 지 판단해서 스크립트 파일이 프로그램 시작점과 맞는지 판단)
# 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도
if __name__ == '__main__':
    app.run(debug=True)