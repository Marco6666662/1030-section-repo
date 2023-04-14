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
    quantity int,
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
    start_date date,
    dob date,
    first_name varchar(20),
    last_name varchar(20),
    primary_email varchar(50),
    secondary_email varchar(50),
    gender varchar(10),
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
    discount decimal(3, 1),
    promo_code varchar(50),
    start_date date,
    end_date date,
    PRIMARY KEY(proj_num, proj_name, prod_id),
    CONSTRAINT fk_prod3
                       FOREIGN KEY (prod_id) REFERENCES products (prod_id)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);


-- INSERTS --
insert into departments (name, dept_id, num_employees)
values ('Administration', 1, 5),
       ('Marketing', 2, 10);

insert into customers (cust_id, street, city, state, zip_code, first_name, last_name, email, dob, phone)
values (1, '100 Apple St', 'Boston', 'MA', '02120', 'John', 'Smith', 'jsmith1234@mail.com', '2003-01-01', '123-456-7890'),
       (2, '200 Apple St', 'Boston', 'MA', '02120', 'Jane', 'Smith', 'jsmith1235@mail.com', '2002-01-01', '123-456-7891');

insert into orders (order_status, quantity, order_date, cust_id)
values (1, 1, '2023-04-07', 1),
       (2, 1, '2023-01-01', 2);

insert into employees (salary, ssn, emp_id, street, city, state, zip_code, join_date, start_date, dob,
                       first_name, last_name, primary_email, secondary_email, gender, phone, dept_id)
values (123456.78, '123-45-6789', 1, '100 Banana St', 'Boston', 'MA', 02120, '2020-01-01', '2020-01-01', '2000-01-01',
        'Boss', 'Man', 'ceo@mail.com', 'bossman@mail.com', 'Male', '098-765-4321', 1),
    (50000.00, '987-65-4321', 2, '200 Banana St', 'Boston', 'MA', 02120, '2020-01-01', '2020-01-01', '2002-01-01',
        'Marketing', 'Man', 'marketing1@mail.com', 'marketing1@mail.com', 'Male', '102-394-5867', 2);

insert into projects (name, number, budget, dept_id)
values ('Benchmark Scores', 1, 100000.00, 1),
       ('Project 2', 2, 10.00, 2);

insert into products (date_listed, name, class, category, rating, reviews, price, page_views, description,
                      brought_id, order_id)
values ('2023-01-01', 'Intel i7-13700K', '16 Core', 'CPU', 4.56, 123, 400.00, 10000, 'The latest high-end Intel CPU',
        1, 1),
    ('2023-01-01', 'RTX 4090', 'Nvidia GPU', 'GPU', 1.23, 10, 2000.00, 100000, 'The latest high-end Nvidia GPU',
        2, 2);

insert into retailers (name, rating, reviews, street, city, state, zip_code, email, proj_num, proj_name)
values ('PC Part Sellers LLC', 3.45, 100, '1 Orange Dr', 'Cityville', 'NY', '12345', 'pps@pps.com', 1, 'Benchmark Scores'),
       ('Bruh LLC', 5.00, 99999, '1 Bruh St', 'Bruhtown', 'BR', '99999', 'bruh@bruh.com', 2, 'Project 2');

insert into emp_project (emp_id, proj_num, proj_name, start_date, hour)
values (1, 1, 'Benchmark Scores', '2023-01-01', 100.00),
       (2, 2, 'Project 2', '2023-01-01', 1.00);

insert into fulfilled (ret_id, order_id)
values (1, 1),
       (2, 2);

insert into offered_by (ret_id, product_id, stock)
values (1, 1, 100),
       (2, 2, 0);

insert into order_products (order_id, product_id)
values (1, 1),
       (2, 2);

insert into promotions (proj_num, proj_name, prod_id, discount, promo_code, start_date, end_date)
values (1, 'Benchmark Scores', 1, 20.0, 'QWERTYUIOP1234567890', '2023-01-01', '2023-12-31'),
       (2, 'Project 2', 2, 99.9, 'ZXCVBNM0987654321', '2023-01-01', '2023-12-31');=
