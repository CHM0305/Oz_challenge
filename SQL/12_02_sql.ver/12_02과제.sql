-- employees 테이블 생성
create table employees(
	id int auto_increment primary key,
    name varchar(100),
    position varchar(100),
    salary decimal(10,2)
);
-- 테이블 확인
desc employees;

-- error 1157 해결 방법 안전문을 껐다 켰다하면 됨(데이터 업데이트가 안됨. 해결 완)
SET SQL_SAFE_UPDATES = 0;
SET SQL_SAFE_UPDATES = 1;

-- employees 테이블에 직원데이터 추가
insert into employees(name,position,salary)value("혜린","PM",90000),("은우","Frontend",80000),("가을","Backend",92000),("지수","Frontend",78000),("민혁","Frontend",96000),("하은","Backend",130000);

-- 직급이 프론트엔드에 월급이 90000 미만인 사람 이름과 직급 출력하기
select name, position from employees where salary<90000 and position="Frontend";

-- 직급이 PM인 사람에게 월급 10% 인상
update employees set salary = salary * 1.1 where position = "PM" ;

-- 직급이 Backend인 사람에게 월급 5% 인상
update employees set salary = salary * 1.05 where position = "Backend";
select position,name,salary from employees;

-- 민혁 사원의 데이터 삭제 
delete from employees where name="민혁";

-- 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산
select position,avg(salary),sum(salary)/3 from employees group by position;
-- 왜 가격이 다른건지..?


-- employees 테이블을 삭제하시오.
delete from employees;
