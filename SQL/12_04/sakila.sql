-- 특정 배우가 출연한 영화 목록 조회
select f.title
from film f
join film_actor fa on fa.film_id=f.film_id
join actor a on a.actor_id=fa.actor_id
where a.first_name="PENELOPE" and a.last_name="GUINESS";

-- 모든 카테고리와 해당 카테고리의 영화 수 조회
select c.name, count(fc.film_id) as categoryCount
from category c 
join film_category fc on fc.category_id=c.category_id
group by c.name;

-- 특정 고객의 대여 기록 조회
select r.rental_date, f.title
from rental r
join inventory i on r.inventory_id=i.inventory_id
join film f on i.film_id=f.film_id
where r.customer_id=5;

-- 가장 최근에 추가된 10개의 영화 조회
select title from film order by release_year desc limit 10;

-- 특정 영화에 출연한 배우 목록 조회(필름, 필름_배우/영화 아이디, 배우)
select a.first_name,a.last_name, f.title
from film_actor fa
join film f on fa.film_id=f.film_id
join actor a on a.actor_id=fa.actor_id
where f.title="ACADEMY DINOSAUR";

-- 특정 영화를 대여한 고객 목록 조회(필름 인벤토리 렌탈 고객) %%DISTINCT
select DISTINCT c.first_name, c.last_name
from customer c
join rental r on c.customer_id=r.customer_id
join inventory i on i.inventory_id= r.inventory_id
join film f on f.film_id=i.film_id
where f.title="ACADEMY DINOSAUR";

-- 모든 고객과 그들이 가장 최근에 대여한 영화 조회
select c.customer_id,c.first_name, c.last_name, r.rental_date, f.title 
from customer c 
join rental r on r.customer_id=c.customer_id
join inventory i on i.inventory_id= r.inventory_id
join film f on f.film_id=i.film_id
where r.rental_date=(
	select MAX(rr.rental_date)
    from rental rr 
    where rr.customer_id = c.customer_id
);

-- 각 영화별 평균 대여 기간 조회
	select f.title, AVG(DATEDIFF(r.return_date,r.rental_date)) as totaldate
    from film f
    join inventory i on i.film_id=f.film_id
    join rental r on r.inventory_id=i.inventory_id
    group by f.title;
-- 	select f.title, r.rental_date as totaldate
--     from film f
--     join inventory i on i.film_id=f.film_id
--     join rental r on r.inventory=i.inventory
--     group by f.title
--     where totaldate=r.return_date-r.rental_date;
    
-- 가장 많이 대여된 영화 조회
	select f.title, count(r.rental_id) as rental_count
    from film f 
    join inventory i on f.film_id = i.film_id
    join rental r on i.inventory_id = r.inventory_id
    group by f.title
    order by rental_count desc
    limit 1;
    
-- 각 카테고리별 평균 대여 요금 조회
select c.name, avg(f.rental_rate) as total_rate
from category c 
join film_category fc on fc.category_id=c.category_id
join film f on fc.film_id=f.film_id
group by c.name;

-- 월별 총 매출 조회
select sum(amount), substr(payment_date,1,7) as total_payment
from payment
group by total_payment;

-- 각 배우별 출연한 영화 수 조회
select a.first_name, a.last_name, count(fa.film_id) as total_film
from actor a
join film_actor fa on a.actor_id=fa.actor_id
group by a.first_name, a.last_name;

-- 가장 수익이 많은 영화 조회
select f.title, sum(p.amount) as total_amount
from film f
join inventory i on f.film_id=i.film_id
join rental r on r.inventory_id=i.inventory_id
join payment p on p.rental_id=r.rental_id
group by f.title
order by total_amount desc limit 1;

-- 평균 대여 요금보다 높은 요금의 영화 조회
select f.title, f.rental_rate
from film f
where f.rental_rate>(select avg(rental_rate) from film);

-- 가장 활동적인 고객 조회
select c.customer_id, c.first_name, c.last_name, count(r.rental_id) as total_count
from customer c
join rental r on r.customer_id=c.customer_id
group by c.customer_id
order by total_count desc limit 1;

-- 특정 배우가 출연한 영화 중 가장 인기 있는 영화 조회
select f.title, count(r.rental_id) as count_rental
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
where a.first_name="PENELOPE" and a.last_name="GUINESS"
group by f.title
order by count_rental desc limit 1;

-- 새로운 영화 추가
insert into film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features) 
values ('New Adventure Movie', 'New Acting',2021,2,3,2.43,120, 19.99, 'PG', 'Trailers,Commentaries');

-- 고객 정보 업데이트
update customer c join address a on a.address_id=c.address_id 
set a.address="123 New Address, New City"  where c.customer_id=5;

-- 영화 대여 상태 변경
update rental set rental_date=now() where rental_id=200;


-- 배우 정보 삭제
delete from actor where actor_id=10;
