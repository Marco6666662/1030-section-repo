create database circuitmart;
show databases;
use circuitmart;

create table employees (
    salary decimal(13, 2),
    ssn varchar(11),
    emp_id int PRIMARY KEY AUTO_INCREMENT,
    street varchar(50),
    city varchar(50),
    state varchar(50),
    zip_code varchar(10),
    join_date date,
    start_date date,
    dob date,
    first_name varchar(20),
    last_name varchar(20),
    primary_email varchar(50),
    secondary_email varchar(50),
    gender varchar(10),
    phone varchar(20),
    dept_id int not null,
    CONSTRAINT fk_dept1
                       FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table departments (
    name varchar(50),
    dept_id int PRIMARY KEY AUTO_INCREMENT,
    num_employees int
);

create table projects (
    name varchar(50),
    number int AUTO_INCREMENT,
    budget decimal(13, 2),
    dept_id int,
    PRIMARY KEY(name, number),
    CONSTRAINT fk_dept2
                      FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
                      ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_num1
                       FOREIGN KEY (number) REFERENCES retailers (proj_num)
                       ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_name1
                       FOREIGN KEY (name) REFERENCES retailers (proj_name)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table products (
    prod_id int PRIMARY KEY AUTO_INCREMENT,
    date_listed date,
    name varchar(100),
    class varchar(50),
    category varchar(50),
    rating decimal(3, 2),
    reviews int,
    price decimal(13, 2),
    page_views int,
    description mediumtext,
    brought_id int,
    order_id int,
    CONSTRAINT fk_brought
                       FOREIGN KEY (brought_id) REFERENCES products (prod_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_order
                       FOREIGN KEY (order_id) REFERENCES orders (order_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table orders (
    order_status int,
    quantity int,
    order_date date,
    order_id int PRIMARY KEY AUTO_INCREMENT
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
    proj_name varchar(100)
);

create table emp_project (
    emp_id int,
    proj_num int,
    proj_name varchar(100),
    start_date date,
    hour decimal(6, 2),
    PRIMARY KEY(emp_id, proj_name, proj_name),
    CONSTRAINT fk_proj_num
                         FOREIGN KEY (proj_num) REFERENCES projects (number)
                         ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_proj_name
                       FOREIGN KEY (proj_name) REFERENCES projects (name)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table fulfilled (
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

create table offered_by (
    ret_id int,
    product_id int,
    stock int,
    PRIMARY KEY(ret_id, product_id),
    CONSTRAINT fk_ret2
                       FOREIGN KEY (ret_id) REFERENCES retailers (ret_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_prod2
                       FOREIGN KEY (product_id) REFERENCES products (prod_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table order_products (
    order_id int,
    product_id int,
    PRIMARY KEY(order_id, product_id),
    CONSTRAINT fk_order2
                       FOREIGN KEY (order_id) REFERENCES orders (order_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_prod4
                       FOREIGN KEY (product_id) REFERENCES products (prod_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

create table promotions (
    proj_num int,
    proj_name varchar(100),
    prod_id int,
    discount decimal(3, 2),
    promo_code varchar(50),
    start_date date,
    end_date date,
    PRIMARY KEY(proj_num, proj_name, prod_id),
    CONSTRAINT fk_prod3
                       FOREIGN KEY (prod_id) REFERENCES products (prod_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);


