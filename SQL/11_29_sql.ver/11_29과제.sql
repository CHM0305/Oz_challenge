USE fishbread_db;

create table users(
	user_id int primary key auto_increment,
    name varchar(255) not null,
    age int not null,
    email varchar(100) unique,
    is_business varchar(100) default false
);

create table orders(
	order_id int primary key auto_increment,
    order_date date,
    amount decimal(10,2),
    user_id int,
    foreign key (user_id) references users(user_id)
);

create table inventory(
	item_id int primary key auto_increment,
    item_name varchar(255) not null,
    quantity int not null
);
create table sales(
	sale_id int primary key auto_increment,
    item_id int,
    order_id int,
    foreign key (item_id) references inventory(item_id),
    foreign key (order_id) references orders(order_id),	
    quantity_sold int not null
);
create table daily_sales(
	date date primary key,
    total_sales decimal(10,2) not null
);
