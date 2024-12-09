from pymongo import MongoClient
from datetime import datetime

# MongoDB 서버에 연결 (로컬 서버를 사용 중)
client = MongoClient('mongodb://localhost:27017/')
db = client.local  # 'local' 데이터베이스 선택

# ------------------------- 함수들 정의 -------------------------

# 1. 특정 장르의 책 검색
def find_books_by_genre(db, genre):
    """
    특정 장르(genre)의 책을 검색하고 책 제목과 저자만 출력.
    """
    books_collection = db.books  # 'books' 컬렉션 지정
    query = {"genre": genre}  # 검색 조건: 'genre' 필드가 특정 장르와 일치
    projection = {"_id": 0, "title": 1, "author": 1}  # '_id' 제외, 'title'과 'author'만 가져오기

    # 조건에 맞는 책들을 찾아서 출력
    books = books_collection.find(query, projection)
    for book in books:
        print(book)

# 함수 실행 예시
find_books_by_genre(db, "fantasy")  # 'fantasy' 장르의 책 검색


# 2. 감독별 영화 평균 평점 계산
def calculate_average_ratings(db):
    """
    영화 데이터를 감독별로 그룹화하고 평균 평점을 계산한 뒤 내림차순으로 정렬.
    """
    movies_collection = db.movies  # 'movies' 컬렉션 지정
    pipeline = [
        {"$group": {"_id": "$director", "average_rating": {"$avg": "$rating"}}},  # 감독별 그룹화 + 평균 평점 계산
        {"$sort": {"average_rating": -1}}  # 평균 평점을 기준으로 내림차순 정렬
    ]

    # 집계 파이프라인 실행 후 결과 출력
    results = movies_collection.aggregate(pipeline)
    for result in results:
        print(result)

# 함수 실행 예시
calculate_average_ratings(db)


# 3. 특정 사용자가 최근에 한 행동 조회
def find_recent_actions_by_user(db, user_id, limit=5):
    """
    특정 사용자가 최근 수행한 행동을 조회 (최신순으로 정렬 후 최대 'limit'개 출력).
    """
    user_actions_collection = db.user_actions  # 'user_actions' 컬렉션 지정
    query = {"user_id": user_id}  # 검색 조건: 특정 'user_id'
    sort_criteria = [("timestamp", -1)]  # 'timestamp' 필드 기준 내림차순 정렬

    # 조건에 맞는 행동을 검색하고 최신순으로 정렬, 결과 제한
    actions = user_actions_collection.find(query).sort(sort_criteria).limit(limit)
    for action in actions:
        print(action)

# 함수 실행 예시
find_recent_actions_by_user(db, 1)  # 사용자 ID 1의 최근 5개 행동 조회


# 4. 발행 연도별 책 개수 계산
def count_books_by_year(db):
    """
    책 데이터를 발행 연도별로 그룹화하고, 각 연도의 책 개수를 계산해 출력.
    """
    books_collection = db.books  # 'books' 컬렉션 지정
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},  # 연도별 그룹화 + 책 개수 세기
        {"$sort": {"count": -1}}  # 책 개수를 기준으로 내림차순 정렬
    ]

    # 집계 파이프라인 실행 후 결과 출력
    results = books_collection.aggregate(pipeline)
    for result in results:
        print(result)

# 함수 실행 예시
count_books_by_year(db)


# 5. 특정 조건을 만족하는 사용자 행동 수정
def update_user_actions_before_date(db, user_id, date, old_action, new_action):
    """
    특정 사용자의 행동을 조건에 따라 업데이트:
    - 지정된 날짜 이전에 발생한 특정 행동(old_action)을 새로운 행동(new_action)으로 변경.
    """
    user_actions_collection = db.user_actions  # 'user_actions' 컬렉션 지정
    query = {"user_id": user_id, "action": old_action, "timestamp": {"$lt": date}}  # 조건: user_id, old_action, 날짜 조건
    update = {"$set": {"action": new_action}}  # 'action' 필드 값을 새로 설정

    # 조건에 맞는 도큐먼트 업데이트
    result = user_actions_collection.update_many(query, update)
    print(f"Updated {result.modified_count} documents.")  # 수정된 도큐먼트 개수 출력

# 함수 실행 예시
update_user_actions_before_date(db, 1, datetime(2023, 4, 13), "view", "seen")  
# 사용자 ID 1이 2023년 4월 13일 이전에 수행한 'view' 행동을 'seen'으로 변경
