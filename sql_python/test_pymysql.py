import pymysql

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# CRUD- SELECT * FROM

def get_customers():
    cursor=connection.cursor()

    sql="SELECT*FROM customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers : ", customers)
    print("customers : ", customers['customerNumber'])
    print("customers : ", customers['customerName'])
    print("customers : ", customers['country'])
    cursor.close()


# INSERT INTO
def add_customer():
    cursor=connection.cursor()

    name='inseop'
    family_name='kim'
    sql=f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES (1006,'{name}','{family_name}')"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

add_customer()