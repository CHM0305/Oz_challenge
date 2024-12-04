use classicmodels;
select * from customers;


/*초급 생성 문제*/
-- 고객 추가
insert into customers(customerNumber,customerName,contactLastName)values(1000,"minsu","Park");
-- 제품추가
insert into products(productCode,productName) values (S10_1233,"dall");
-- 직원 추가
insert into employees(employeeNumber, lastName)values(12341,"bey");
-- 사무실 추가
insert into offices(officeCode, city, country, phone)values();
-- 주문 추가
insert into orders(orderNumber,orderDate)values();
-- 주문 상세 정보 추가
insert into orderdetails(orderNumber,quantityOrdered,orderLineNumber)values();
-- 지불 정보 추가
insert into payments(checkNumber,paymentDate,amount)values();
-- 제품 라인 추가
insert into productlines(productLine,textDescription)values();
-- 다른 지역의 고객 추가
insert into customers(customerNumber,customerName,contactLastName,country)values(1001,"min","Leo","Seoul");
-- 다른 카테고리 제품 추가
insert into products(productCode,productName,productLine)values(D_1231, car, 4536);



/*초급 읽기 문제*/
-- 모든 고객 정보 조회
select * from customers;
-- 모든 제품 목록 조회
select productName , productLine from products;
-- 모든 직원 이름, 직급 조회
select lastName,firstName,jobTitle from employees;
-- 모든 사무실 위치 조회
select employeeNumber,city,addressLine1,country from offices;
-- 최근 10개의 주문 조회
select orders order by orderDate desc limit 10 ;
-- 특정 주문의 모든 상세 정보를 조회
select * from orderdetails where orderNumber=3;
-- 특정 고객의 모든 지불 정보를 조회
select * from payments where customerNumber=1;
-- 각 제품 라인의 설명을 조회
select productLine,textDescription from Productlines;
-- 특정 지역의 고객을 조회
select * from customers where country="New york";
-- 특정 가격 범위의 제품을 조회
select * from products where buyPrice>10000;

/*초급 갱신 문제*/
-- 특정 고객의 주소 갱신
update customers set addressLine1="" where customerNumber=1;
-- 특정 제품의 가격 갱신
update products set buyPrice=15000 where productLine="";
-- 특정 직원의 직급을 갱신
update employees set jobtitle="" where officeCode=234;
-- 특정 사무실의 전화번호 갱신
update offices set phone="+2234" where county="";
-- 특정 주문의 상태를 갱신
update orders set requiredDate="" where orderDate="";
-- 특정 주문 상세의 수량을 갱신
update ordersdetails set priceEach=2 where productLine=3;
-- 특정 지불의 금액을 갱신
update payments set amount=14000 where checkNumber=3;
-- 특정 제품 라인의 설명을 갱신
update Productlines set textDescription="" where productLine=43;
-- 특정 고객의 이메일을 갱신
update customers set email="" where customerName="";
-- 여러 제품의 가격을 한번에 갱신
update products set buyPrice=14200 where productLine="";


/*초급 삭제 문제*/
-- 특정 고객 삭제
delete from customers where customerName="";
-- 특정 제품 삭제
delete from products where productName="";
-- 특정 직원 삭제
delete from employees where employeeNumber=234;
-- 특정 사무실 삭제
delete from offices where officeCode=234; 
-- 특정 주문 삭제
delete from orders where orderNumber=234;
-- 특정 주문 상세 삭제
delete from orderdetails where orderNumber=23; 
-- 특정 지불 내역 삭제
delete from payments where paymentDate="2024-03-24"; 
-- 특정 제품 라인 삭제
delete from products where productLine="";
-- 특정 지역의 모든 고객 삭제
delete from customers where country="";
-- 특정 카테고리의 모든 제품 삭제
delete from products where productLine="";
SELECT VERSION();