DROP SCHEMA IF EXISTS supermarket;
CREATE SCHEMA supermarket;
USE supermarket;

CREATE TABLE drink(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    expiration_date DATETIME,
    is_available BOOL    
);

INSERT INTO drink(name, expiration_date, is_available) VALUES
	('coffee','2026-5-27', TRUE),
    ('water','2026-12-27', FALSE),
	('beer','2028-2-29', TRUE);


CREATE TABLE orders(
	id INT AUTO_INCREMENT PRIMARY KEY,
    vendor VARCHAR(255),
    drink_id INT,
    quantity INT,
    FOREIGN KEY (drink_id) REFERENCES drink(id)    
);

INSERT INTO orders(vendor, drink_id, quantity) VALUES
	('Ana',1, 5),
    ('Marta',1, 10),
    ('Marta',3, 25),
    ('Isabel',3, 25),
    ('Isabel',1, 100),
    ('Pablo',2, 19),
    ('Raul',3, 12),
    ('Raul',2, 48),
	('Gustavo',2, 24);
    
    -- queries con boolenos
    
SELECT * FROM drink WHERE is_available IS TRUE;
SELECT * FROM drink WHERE is_available; -- para los booleanos se simplifica la sintaxisa

select name, extract(MONTH FROM expiration_date) AS mes FROM drink WHERE is_available;

-- fecha actual
SELECT curdate();
SELECT current_time();
SELECT current_user();    

-- operaciones sobre fechas
SELECT date_add(curdate(), INTERVAL 2 day) AS dentro_de_2_dias;

SELECT date_add(current_time(), INTERVAL 2 minute) AS dentro_de_2_minutos;
SELECT addtime(current_time(), '12:25:29') AS dentro_de_2_minutos;

select current_time() + interval 2 minute AS dentro_de_2_minutos;

-- subconsultas
-- inicial
select * from orders;
select vendor, sum(quantity) as total from orders GROUP BY vendor;
-- redaccion subconsultas
select opv.vendor, opv.total 
FROM (select vendor, sum(quantity) as total from orders GROUP BY vendor) opv
where opv.total >15;

-- otra manera dedeclara subconsultas:
with orders_per_vender AS (select vendor, sum(quantity) as total from orders GROUP BY vendor)
select vendor, total
from orders_per_vender
where total >15;

-- subconsulta con join
with order_per_vendor AS (select vendor, sum(quantity) as total from orders group by vendor)
SELECT o.vendor, d.name, o.quantity 
FROM orders o
join drink d on d.id = o.drink_id
join order_per_vendor opv on opv.vendor = o.vendor
where opv.total > 15;

-- agregacion sobre sunconsulta
with order_per_vendor AS (select vendor, sum(quantity) as total from orders group by vendor)
SELECT o.vendor, d.name, sum(o.quantity) 
FROM orders o
join drink d on d.id = o.drink_id
join order_per_vendor opv on opv.vendor = o.vendor
where opv.total > 15
group BY o.vendor, d.name;