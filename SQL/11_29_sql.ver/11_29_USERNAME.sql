-- USE test;users
CREATE TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY, -- 주요식별자 정의 (검색속도 향상을 위해), 숫자 자동증가 속성을 가짐(id 갑이 1씩 증가.): 아이디를 숫자로 만들거고 고유한 값을 설절해줄꺼얌
	username VARCHAR(50) NOT NULL, -- 비어있는 값은 입력이 불가능하단 것도 설정해줌.
	email VARCHAR(100) UNIQUE, -- 유니크 설정
    is_business VARCHAR(10) DEFAULT False, -- 비즈니스 계정인지 아닌지 확인하는 것으로 처음은 무조건 False
	age INT CHECK (age >= 10) -- 체크(조건),더블 체킹을 위함! 웹프레임워크, db에 넣을때도 다시 한번 확인하기 위함.
);