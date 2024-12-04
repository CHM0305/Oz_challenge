import pymysql
import pymysql.cursors

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='1234',  # 데이터베이스 비밀번호
    db='airbnb',       # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # 1)새로운 제품 추가
        # sql="INSERT INTO Products(productID,productName,price,stockQuantity)VALUES(%s,%s,%s,%s)"
        # cursor.execute(sql,(21,"Python Book",29.99,85))
        # conn.commit()

        # 2)고객 목록 조회
        # sql = "SELECT * FROM Customers"
        # cursor.execute(sql)
        # for i in cursor.fetchall():
        #     print(i)

        # 3) 제품 재고 업데이트
        # sql="UPDATE Products SET stockQuantity=stockQuantity-1 WHERE productName=(%s)"
        # cursor.execute(sql,"Python Book")
        # conn.commit()

        # 4) 고객별 총 주문 금액 계산
        # sql="SELECT customerID, sum(totalAmount) FROM Orders GROUP BY customerID"
        # cursor.execute(sql)
        # for i in cursor.fetchall():
        #     print(i)

        # 5) 고객 이메일 업데이트
        # sql="UPDATE Customers SET email=(%s) WHERE customerName=(%s)"
        # cursor.execute(sql,("abcd@gmail.com","James Diaz"))
        # conn.commit()

        # 6) 주문 취소
        # sql="DELETE FROM Orders WHERE orderID=(%s)"
        # cursor.execute(sql,30)
        # conn.commit()

        # 7) 특정 제품 검색
        # sql="SELECT productName, price FROM Products WHERE productName=(%s)"
        # cursor.execute(sql,"Python Book")
        # for i in cursor.fetchall():
        #     print(i)

        # LIKE 이용하기 
        # sql="SELECT * FROM Products WHERE productName LIKE %s"
        # cursor.execute(sql,('%Book%'))
        # for i in cursor.fetchall():
        #     print(i)



        # 8) 특정 고객의 모든 주문 조회
        # sql="SELECT orderDate, totalAmount FROM Orders WHERE orderID=(%s)"
        # cursor.execute(sql,3)
        # for i in cursor.fetchall():
        #     print(i)

        # 9) 가장 많이 주문한 고객 찾기
        # sql="SELECT customerID FROM Orders WHERE sum(customerID)" 모르겠음!!
        """먼저 Orders테이블로부터 중요한 많이 주문한 고객아이디와 주문수(별칭 orderCount)를 불러올꺼고,
        주문수를 측정하기 위해선 우선 고객 아이디를 그룹화하고 
        그룹화한 아이디의 주문수들을 내림차순으로 정렬하고
        그 중 하나의 컬럼만 추출하면 됨."""
        sql = "SELECT customerID, COUNT(*) as orderCount FROM Orders GROUP BY customerID ORDER BY orderCount DESC LIMIT 1"
        cursor.execute(sql)
        top_customer = cursor.fetchone()
        print(f"Top Customer ID: {top_customer['customerID']}, Orders: {top_customer['orderCount']}")

finally:
    conn.close()