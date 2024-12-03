use classicmodels;
select * from classicmodels;
/*기본 조회 및 필터링*/
-- 고객 목록 조회
select customerName from customers;

-- 특정 제품 라인의 제품 조회, 제품라인이 클래식 차인 것들만 조회해줘
select * from products
where productLine ="classic Cars";

-- 최근 주문, 주문 날짜를 10개로 목록 정리해서 조회해줘
select * from orders order by orderdate desc limit 10;

-- 최소 금액 이상의 결제, 가격이 100보다 많은 것들만 조회해줘
select* from payments where amount>=100;

/* 조인 쿼리 */
-- 주문과 고객 정보 조합, 주문과 고객 테이블이 필요함
select o.ordernumber, c.customername from orders o join customers c on c.customerNumber=o.customerNumber;

-- 제품과 제품 라인 결합
SELECT p.productName, p.productLine, pl.textDescription FROM products p
JOIN productlines pl ON p.productLine = pl.productLine;

-- 직원과 상사 정보
SELECT e1.employeeNumber, e1.firstName, e1.lastName, e2.firstName AS 'ManagerFirstName', e2.lastName AS 'ManagerLastName'
FROM employees e1
LEFT JOIN employees e2 ON e1.reportsTo = e2.employeeNumber;

-- 특정 사무실의 직원 목록
SELECT e.employeeNumber, e.lastName, e.firstName, e.extension, e.email, e.officeCode, e.reportsTo, e.jobTitle
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
WHERE o.city = 'San Francisco';

/*그룹 쿼리*/
-- 제품 라인별 제품 수
SELECT productLine, COUNT(*) AS productCount
FROM products
GROUP BY productLine;

-- 고객별 총 주문 금액
SELECT customers.customerNumber, 
       customers.customerName, 
       SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS totalAmount
FROM customers
JOIN orders ON customers.customerNumber = orders.customerNumber
JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
GROUP BY customers.customerNumber, customers.customerName;

-- 가장 많이 팔린 제품
SELECT productName, SUM(quantityOrdered) AS totalQuantity
FROM orderdetails od
JOIN products p ON od.productCode = p.productCode
GROUP BY productName
ORDER BY totalQuantity DESC
LIMIT 1;

-- 매출이 가장 높은 사무실
SELECT o.city, SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM orders ord
JOIN orderdetails od ON ord.orderNumber = od.orderNumber
JOIN customers c ON ord.customerNumber = c.customerNumber
JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
JOIN offices o ON e.officeCode = o.officeCode
GROUP BY o.city
ORDER BY totalSales DESC
LIMIT 1;

/*서브쿼리*/
-- 특정 금액 이상의 주문
SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount
FROM orderdetails
GROUP BY orderNumber
HAVING totalAmount > 500;

-- 평균 이상 결제 고객
SELECT customerNumber, SUM(amount) AS totalPayment
FROM payments
GROUP BY customerNumber
HAVING totalPayment > (SELECT AVG(amount) FROM payments);


-- 주문 없는 고객
SELECT customerName
FROM customers
WHERE customerNumber NOT IN (SELECT customerNumber FROM orders);


-- 최대 매출 고객
SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS totalSpent
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY c.customerName
ORDER BY totalSpent DESC
LIMIT 1;

/*데이터 수정 및 관리*/
-- 신규 고객 추가
INSERT INTO customers (customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES ('New Customer', 'Lastname', 'Firstname', '123-456-7890', '123 Street', 'Suite 1', 'City', 'State', 'PostalCode', 'Country', 1002, 50000.00);

-- 제품 가격 변경
UPDATE products
SET buyPrice = buyPrice * 1.10
WHERE productLine = 'Classic Cars';

-- 고객 데이터 업데이트
UPDATE customers
SET email = 'newemail@example.com'
WHERE customerNumber = 103;

-- 직원 전보 
UPDATE employees
SET officeCode = '2'
WHERE employeeNumber = 1002;