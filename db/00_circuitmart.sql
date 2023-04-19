create database circuitmart;
grant all privileges on circuitmart.* to 'webapp'@'%';
flush privileges;
show databases;
use circuitmart;

-- TABLES --
create table departments (
    name varchar(50),
    dept_id int PRIMARY KEY AUTO_INCREMENT,
    num_employees int
);

create table customers (
    cust_id int PRIMARY KEY AUTO_INCREMENT,
    street varchar(50),
    city varchar(50),
    state varchar(50),
    zip_code varchar(10),
    first_name varchar(20),
    last_name varchar(20),
    email varchar(50),
    dob date,
    phone varchar(20)
);

create table orders (
    order_status int,
    order_date date,
    order_id int PRIMARY KEY AUTO_INCREMENT,
    cust_id int,
    CONSTRAINT fk_dept1
                       FOREIGN KEY (cust_id) REFERENCES customers (cust_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table employees (
    salary decimal(13, 2),
    ssn varchar(11),
    emp_id int PRIMARY KEY AUTO_INCREMENT,
    street varchar(50),
    city varchar(50),
    state varchar(50),
    zip_code varchar(10),
    join_date date,
    dob date,
    first_name varchar(20),
    last_name varchar(20),
    primary_email varchar(50),
    secondary_email varchar(50),
    gender varchar(20),
    phone varchar(20),
    dept_id int not null,
    CONSTRAINT fk_dept2
                       FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table projects (
    name varchar(50),
    number int,
    budget decimal(13, 2),
    dept_id int,
    PRIMARY KEY(name, number),
    CONSTRAINT fk_dept3
                      FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
                      ON UPDATE CASCADE ON DELETE RESTRICT
);

create table products (
    prod_id int PRIMARY KEY AUTO_INCREMENT,
    date_listed date,
    prod_name varchar(100),
    prod_class varchar(50),
    category varchar(50),
    rating decimal(3, 2),
    reviews int,
    price decimal(13, 2),
    page_views int,
    description mediumtext
);

create table retailers (
    ret_id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(50),
    rating decimal(3, 2),
    reviews int,
    street varchar(50),
    city varchar(50),
    state varchar(50),
    zip_code varchar(10),
    email varchar(50),
    proj_num int,
    proj_name varchar(50),
    CONSTRAINT fk_proj1
                       FOREIGN KEY (proj_name,proj_num) REFERENCES projects(name,number)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table emp_project (
    emp_id int,
    proj_num int,
    proj_name varchar(100),
    start_date date,
    hour decimal(6, 2),
    PRIMARY KEY(emp_id, proj_name, proj_num),
    CONSTRAINT fk_proj2
                         FOREIGN KEY (proj_name,proj_num) REFERENCES projects (name,number)
                         ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_emp_proj
                         FOREIGN KEY (emp_id) REFERENCES employees (emp_id)
                         ON UPDATE CASCADE ON DELETE RESTRICT
);

create table fulfillment (
    ret_id int,
    order_id int,
    PRIMARY KEY(ret_id, order_id),
    CONSTRAINT fk_ret1
                       FOREIGN KEY (ret_id) REFERENCES retailers (ret_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_order1
                       FOREIGN KEY (order_id) REFERENCES orders (order_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table retailers_products (
    ret_id int,
    prod_id int,
    stock int,
    PRIMARY KEY(ret_id, prod_id),
    CONSTRAINT fk_ret2
                       FOREIGN KEY (ret_id) REFERENCES retailers (ret_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_prod2
                       FOREIGN KEY (prod_id) REFERENCES products (prod_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table order_products (
    order_id int,
    prod_id int,
    quantity int,
    PRIMARY KEY(order_id, prod_id),
    CONSTRAINT fk_order2
                       FOREIGN KEY (order_id) REFERENCES orders (order_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_prod4
                       FOREIGN KEY (prod_id) REFERENCES products (prod_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table promotions (
    proj_num int,
    proj_name varchar(100),
    prod_id int,
    discount decimal(3, 1),
    promo_code varchar(50),
    start_date date,
    end_date date,
    PRIMARY KEY(proj_num, proj_name, prod_id),
    CONSTRAINT fk_prod3
                       FOREIGN KEY (prod_id) REFERENCES products (prod_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_proj3
                         FOREIGN KEY (proj_name,proj_num) REFERENCES projects (name,number)
                         ON UPDATE CASCADE ON DELETE RESTRICT
);
