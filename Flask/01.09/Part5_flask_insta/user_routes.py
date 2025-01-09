# user_model.py - 사용자 데이터 및 관련 함수 정의

# 초기 사용자 데이터를 포함하는 리스트
users = [
    {"username": "leo", "posts": [{"title": "Town House", "likes": 120}]},
    {"username": "alex", "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]},
    {"username": "kim", "posts": [{"title": "Delicious Ramen", "likes": 230}]}
]

# 새로운 사용자를 추가하는 함수
def add_user(request_data):
    new_user = {"username": request_data["username"], "posts": []}  # 초기 게시물이 없는 새 사용자 생성
    users.append(new_user)  # 사용자 리스트에 추가
    return new_user, 201  # 생성된 사용자와 HTTP 201 상태 코드 반환

# 특정 사용자의 게시물을 추가하는 함수
def add_post_to_user(username, request_data):
    for user in users:  # 모든 사용자를 순회하며
        if user["username"] == username:  # 일치하는 사용자를 찾으면
            new_post = {"title": request_data["title"], "likes": 0}  # 새 게시물 생성 (좋아요 수 초기화)
            user["posts"].append(new_post)  # 사용자 게시물 목록에 추가
            return new_post, 201  # 생성된 게시물과 HTTP 201 상태 코드 반환
    return {"message": "User not found"}, 404  # 사용자 미발견 시 오류 메시지 반환

# 특정 사용자의 게시물 목록을 조회하는 함수
def get_user_posts(username):
    for user in users:  # 모든 사용자를 순회하며
        if user["username"] == username:  # 일치하는 사용자를 찾으면
            return {"posts": user["posts"]}  # 해당 사용자의 게시물 목록 반환
    return {"message": "User not found"}, 404  # 사용자 미발견 시 오류 메시지 반환

# 특정 게시물의 좋아요 수를 증가시키는 함수
def like_user_post(username, title):
    for user in users:  # 모든 사용자를 순회하며
        if user["username"] == username:  # 일치하는 사용자를 찾으면
            for post in user["posts"]:  # 사용자의 게시물들을 순회하며
                if post["title"] == title:  # 일치하는 게시물을 찾으면
                    post["likes"] += 1  # 좋아요 수 증가
                    return post, 200  # 업데이트된 게시물과 HTTP 200 상태 코드 반환
    return {"message": "Post not found"}, 404  # 게시물 미발견 시 오류 메시지 반환

# 특정 사용자를 삭제하는 함수
def delete_user(username):
    global users  # 전역 users 리스트에 접근
    users = [user for user in users if user["username"] != username]  # 삭제 대상 사용자 제외한 새 리스트 생성
    return {"message": "User deleted"}, 200  # 성공 메시지와 HTTP 200 상태 코드 반환
