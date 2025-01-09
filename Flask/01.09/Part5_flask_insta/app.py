# app.py
from flask import Flask, request

app = Flask(__name__)  # Flask 애플리케이션 초기화

# 사용자 데이터를 저장하는 리스트
users = [
    {"username": "leo", "posts": [{"title": "Town House", "likes": 120}]},
    {"username": "alex", "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]},
    {"username": "kim", "posts": [{"title": "Delicious Ramen", "likes": 230}]},
]

@app.get("/users")  # 모든 사용자 정보를 가져오는 GET 엔드포인트
def get_users():
    return {"users": users}  # JSON 형식으로 모든 사용자 정보 반환

@app.post("/users")  # 새로운 사용자를 생성하는 POST 엔드포인트
def create_user():
    request_data = request.get_json()  # 요청의 JSON 데이터를 추출
    new_user = {"username": request_data["username"], "posts": []}  # 초기 게시물이 없는 사용자 생성
    users.append(new_user)  # 사용자 리스트에 추가
    return new_user, 201  # 생성된 사용자와 HTTP 201 상태 코드 반환

@app.post("/users/post/<string:username>")  # 특정 사용자의 게시물을 추가하는 POST 엔드포인트
def add_post(username):
    request_data = request.get_json()  # 요청 데이터를 추출
    for user in users:  # 사용자를 순회하여
        if user["username"] == username:  # 일치하는 사용자를 찾으면
            new_post = {"title": request_data["title"], "likes": 0}  # 새 게시물 생성
            user["posts"].append(new_post)  # 사용자 게시물 목록에 추가
            return new_post, 201  # 생성된 게시물 반환
    return {"message": "User not found"}, 404  # 사용자 미발견 시 오류 반환

@app.get("/users/post/<string:username>")  # 특정 사용자의 게시물 목록을 반환하는 GET 엔드포인트
def get_posts_of_user(username):
    for user in users:  # 사용자를 순회하여
        if user["username"] == username:  # 일치하는 사용자를 찾으면
            return {"posts": user["posts"]}  # 해당 사용자의 게시물 반환
    return {"message": "User not found"}, 404  # 사용자 미발견 시 오류 반환

@app.put("/users/post/like/<string:username>/<string:title>")  # 특정 게시물의 좋아요 수를 증가시키는 PUT 엔드포인트
def like_post(username, title):
    for user in users:  # 사용자를 순회하여
        if user["username"] == username:  # 일치하는 사용자를 찾으면
            for post in user["posts"]:  # 사용자의 게시물을 순회
                if post["title"] == title:  # 일치하는 게시물을 찾으면
                    post["likes"] += 1  # 좋아요 수 증가
                    return post, 200  # 업데이트된 게시물 반환
    return {"message": "Post not found"}, 404  # 게시물 미발견 시 오류 반환

@app.delete("/users/<string:username>")  # 특정 사용자를 삭제하는 DELETE 엔드포인트
def delete_user(username):
    global users  # 전역 users 리스트 수정
    users = [user for user in users if user["username"] != username]  # 해당 사용자 제외한 새 리스트 생성
    return {"message": "User deleted"}, 200  # 성공 메시지 반환

if __name__ == '__main__':  # 메인 실행일 경우
    app.run(debug=True)  # 디버그 모드로 실행