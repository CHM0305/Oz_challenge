
USE db_test;

CREATE TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(50), 
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL UNIQUE, 
	password VARCHAR(255) NOT NULL, 
	address VARCHAR(255), 
	contact VARCHAR(50), 
	gender ENUM('MALE', 'FEMALE') NOT NULL, 
	is_active BOOLEAN NOT NULL DEFAULT TRUE, 
	is_staff BOOLEAN NOT NULL DEFAULT FALSE 
);

CREATE TABLE stores(
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(50) NOT NULL, 
	address VARCHAR(255), 
	contact VARCHAR(50), 
	is_active BOOLEAN NOT NULL DEFAULT TRUE 
);

CREATE TABLE employees(
	id INT AUTO_INCREMENT PRIMARY KEY,
	code INT NOT NULL UNIQUE, 
	type ENUM('STAFF', 'MANAGER') NOT NULL, 
	user_id INT, 
	store_id INT, 
	is_active BOOLEAN NOT NULL DEFAULT TRUE,
	FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
	FOREIGN KEY (store_id) REFERENCES stores(id) ON DELETE CASCADE
);

CREATE TABLE suppliers(
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(50) NOt NULL,
	address VARCHAR(255), 
	contact VARCHAR(50), 
	is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE raw_materials (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(50) NOT NULL, 
	price DECIMAL(10, 2) NOT NULL 
);

CREATE TABLE products(
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(50) NOT NULL, 
	description TEXT, 
	price DECIMAL(7, 2) NOT NULL 
);

CREATE TABLE stocks(
	id INT AUTO_INCREMENT PRIMARY KEY, 
	raw_material_id INT NOT NULL, 
	pre_quantity INT NOT NULL, 
	quantity INT NOT NULL, 
	change_type ENUM('IN', 'OUT', 'RETURNED', 'DISCARDED'), 
	store_id INT NOT NULL, 
	create_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
	FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id),
	FOREIGN KEY (store_id) REFERENCES stores(id)
);

CREATE TABLE order_records(
	id INT AUTO_INCREMENT PRIMARY KEY,
	employee_id INT, 
	supplier_id INT, 
	change_date DATETIME DEFAULT CURRENT_TIMESTAMP, 
	raw_material_id INT, 
	quantity INT NOT NULL, 
	create_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
	FOREIGN KEY (employee_id) REFERENCES employees(id),
	FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id),
	FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

CREATE TABLE sales_records(
	id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT,
	store_id INT, 
	is_refund BOOL DEFAULT FALSE,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (store_id) REFERENCES stores(id)
);

CREATE TABLE sales_items(
	id INT AUTO_INCREMENT PRIMARY KEY, 
	sales_record_id INT, 
	product_id INT, 
	quantity INT NOT NULL, 
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
	FOREIGN KEY (sales_record_id) REFERENCES sales_records(id),
	FOREIGN KEY (product_id) REFERENCES products(id)
);