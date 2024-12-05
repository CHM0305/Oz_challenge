import random

import pymysql
from faker import Faker
from pymysql.cursors import DictCursor

# Faker 객체 생성
fake = Faker()

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host="localhost",
    user="root",  # 사용자 이름
    password="1234",  # 비밀번호
    database="db_test", # db 이름
    charset="utf8mb4",
    cursorclass=DictCursor,
)

try:
    with connection.cursor() as cursor:
        # 더미 사용자 데이터 삽입
        for _ in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.unique.email()
            password = fake.password()
            address = fake.address()
            contact = fake.phone_number()
            gender = random.choice(["MALE", "FEMALE"])

            cursor.execute(
                """
                INSERT INTO users (first_name, last_name, email, password, address, contact, gender)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
                (first_name, last_name, email, password, address, contact, gender),
            )

        # 더미 가맹점 데이터 삽입
        for _ in range(5):
            name = fake.country()
            address = fake.address()
            contact = fake.phone_number()

            cursor.execute(
                """
                INSERT INTO stores (name, address, contact)
                VALUES (%s, %s, %s)""",
                (name, address, contact),
            )

        # 더미 공급업체 데이터 삽입
        for _ in range(5):
            name = fake.company()
            address = fake.address()
            contact = fake.phone_number()

            cursor.execute(
                """
                INSERT INTO suppliers (name, address, contact)
                VALUES (%s, %s, %s)
            """,
                (name, address, contact),
            )

        # 더미 원재료 데이터 삽입
        raw_materials = [
            ("Flour", 1.76),
            ("Sugar", 2.00),
            ("Yeast", 0.50),
            ("Red Bean Paste", 4.50),
            ("Chocolate", 28.00),
            ("Cream", 4.50),
            ("Avocado", 11.40),
        ]

        for name, price in raw_materials:
            cursor.execute(
                """
                INSERT INTO raw_materials (name, price)
                VALUES (%s, %s)
            """,
                (name, price),
            )

        # 더미 제품 데이터 삽입
        products = [
            ("Fish Bun", "A delicious fish-shaped bun.", 3.00),
            ("Red Bean Bun", "Sweet bun filled with red bean paste.", 2.50),
            ("Chocolate Bun", "Decadent chocolate-filled bun.", 3.50),
            ("Avocado Bun", "Fresh avocado-filled bun.", 5.50),
        ]

        for name, description, price in products:
            cursor.execute(
                """
                INSERT INTO products (name, description, price)
                VALUES (%s, %s, %s)
            """,
                (name, description, price),
            )

        print("all done")
        # 변경 사항 커밋
        connection.commit()
finally:
    connection.close()
