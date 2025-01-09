# user_routes.py - 사용자 관련 라우트를 정의하는 파일
from flask import request  # Flask 요청 객체 가져오기
from user_model import users, add_user, add_post_to_user, get_user_posts, like_user_post, delete_user  # 사용자 관련 기능 가져오기

# Flask 앱에 라우트를 등록하는 함수 정의
def register_routes(app):
    @app.route("/users", methods=["GET", "POST"])  # /users 경로에 GET, POST 메서드 허용
    def users_route():
        if request.method == "GET":  # GET 요청인 경우
            return {"users": users}  # 모든 사용자 데이터를 JSON으로 반환
        elif request.method == "POST":  # POST 요청인 경우
            request_data = request.get_json()  # 요청에서 JSON 데이터 추출
            return add_user(request_data)  # 사용자 생성 함수 호출 및 결과 반환

    @app.route("/users/post/<string:username>", methods=["POST"])  # 특정 사용자의 게시물을 추가하는 POST 엔드포인트
    def add_post(username):
        request_data = request.get_json()  # 요청에서 JSON 데이터 추출
        return add_post_to_user(username, request_data)  # 게시물 추가 함수 호출 및 결과 반환

    @app.route("/users/post/<string:username>", methods=["GET"])  # 특정 사용자의 게시물을 조회하는 GET 엔드포인트
    def get_posts(username):
        return get_user_posts(username)  # 사용자 게시물 조회 함수 호출 및 결과 반환

    @app.route("/users/post/like/<string:username>/<string:title>", methods=["PUT"])  # 특정 게시물 좋아요 수 증가하는 PUT 엔드포인트
    def like_post(username, title):
        return like_user_post(username, title)  # 좋아요 증가 함수 호출 및 결과 반환

    @app.route("/users/<string:username>", methods=["DELETE"])  # 특정 사용자를 삭제하는 DELETE 엔드포인트
    def delete(username):
        return delete_user(username)  # 사용자 삭제 함수 호출 및 결과 반환
