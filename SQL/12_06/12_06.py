import pymysql
from pymysql.cursors import DictCursor

connection = pymysql.connect(
    host="localhost",
    user="root",  # 사용자 이름
    password="1234",  # 비밀번호
    database="db_test", # db 이름
    charset="utf8mb4",
    cursorclass=DictCursor
)


try:
    with connection.cursor() as cursor:
    
    #1. 새로운 사용자 '8kijoa' 추가
        # sql="INSERT INTO users (last_name,email,password,gender,is_active,is_staff)values(%s,%s,%s,%s,%s,%s)"
        # cursor.execute(sql,('8kijoa','8kijoa@naver.com','1234','FEMALE',1,0))
        # connection.commit()


    #2. 사용자 '8kijoa' 주소 변경
        # sql="UPDATE users SET address=(%s) where last_name=(%s)"
        # cursor.execute(sql,('Busan','8kijoa'))
        # connection.commit()

    #3. 1번 store 에서 사용자 '8kijoa'의 주문을 생성(판붕 3-2, 크림붕 2개-10 시그니처 메뉴 5개-9)
        # sql="insert into sales_records(user_id,store_id,is_refund, created_at)values((%s),(%s),0,now())"
        # cursor.execute(sql,((31),(1))) 
        # #유저 아이디- 스토어 아이디 입력( 유저가 스토어에 주문을 한다.)
        # connection.commit()

        # sql="insert into sales_items(sales_record_id,product_id,quantity,created_at)values(2,(%s),(%s),now()),(2,(%s),(%s),now()),(2,(%s),(%s),now())"
        # cursor.execute(sql,((2),(3),(10),(2),(5),(9))) 
        # # 붕어빵- 수량 주문(스토어에서 유저가 주문한 붕어빵을 만든다.)
        # connection.commit()
        
    #4. order_records 테이블에 발주이력을 3건 셍성(재료는 자유롭게)
        # sql="select * from order_records limit %s"
        # cursor.execute(sql,3)
        # result=cursor.fetchmany(3)
        # print(result)
            



    #5. stocks 테이블에 원재료 사용이력 3건 추가, 최근 사용이력 3건 조회
        # sql="""insert into  stocks (raw_material_id,pre_quantity,quantity,change_type,store_id)
        #     values(3,16,56,'IN',3),
        #     (2,80,76,'RETURNED',7),
        #     (4,20,35,'OUT',5)"""
        # cursor.execute(sql)
        # connection.commit()
        # sql="""select id,raw_material_id,pre_quantity,quantity,change_type,store_id,create_at
        #         from stocks order by create_at desc limit %s"""
        # cursor.execute(sql,3)
        # result=cursor.fetchmany(3)
        # print(result)




    #6. 유저 '8kijoa'가 주문한 내역을 조회(단, 비싼 금액의 상품순으로 나열)
        sql="""select u.last_name,p.name,si.quantity ,p.price
        from sales_records s 
        join users u on s.user_id=u.id 
        join sales_items si on si.sales_record_id=s.id
        join products p on p.id=si.product_id
        where u.last_name="8kijoa"
        order by p.price desc;"""
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
        


    print("all done")

    connection.commit()    

finally:
    connection.close()