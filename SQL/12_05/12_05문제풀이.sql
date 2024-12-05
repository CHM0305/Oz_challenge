-- 1번 user 10명 생성
insert into users (last_name,email,password,gender,is_active,is_staff)
values ('Pack','sdf@ads','123','MALE',1,0),
('Ping','xzx@dd','123','FEMALE',1,0),
('Choi','asd@gg','123','MALE',1,0),
('Kim','qmq@ch','123','FEMALE',1,0),
('Ina','ah@chb','123','FEMALE',1,0),
('Eu','th@abx','123','MALE',1,0),
('Yeong','ad@dfb','123','FEMALE',1,0),
('Ro','asd@hou','123','FEMALE',1,0),
('You','wer@jb','123','FEMALE',1,0),
('Gun','oji@fgc','123','MALE',1,0)
;

-- 2번 재고 변동 이력 10개 생성
insert into stocks (raw_material_id,pre_quantity,quantity,change_type,store_id)
values(1,80,150,'IN',1),
(2,40,30,'RETURNED',10),
(3,20,50,'IN',9),
(4,50,35,'OUT',8),
(5,7,0,'DISCARDED',7),
(6,40,50,'IN',6),
(7,70,20,'OUT',5),
(8,20,35,'IN',4),
(9,40,60,'IN',3),
(10,100,70,'OUT',2);

-- 3번 sales_items 테이블에 데이터 추가하기
insert into sales_items(sales_records,product_id,quantity)values(1,9,10);

-- 4번 products 테이블에 시그니처 메뉴 추가하기
insert into products (name,description,price)values("Sweet Poteto Bun","YUMMMMM",3.6);


-- 5번 유저 1를 매장 아이디5에 속하는 직원으로, 유저2를 매장 아이디 7에 속하는 매니저로 업데이트

-- user1 ->stores_id 5

update employees e 
join users u on e.user_id=u.id 
join stores s on s.id=e.store_id
set e.user_id=1 ,e.type="STAFF"
where e.user_id= 10 and e.store_id=5;

-- user2 ->stores_id 7

update employees e 
join users u on e.user_id=u.id 
join stores s on s.id=e.store_id
set e.user_id=2 ,e.type="MANAGER"
where e.user_id=9 and e.store_id=7;
