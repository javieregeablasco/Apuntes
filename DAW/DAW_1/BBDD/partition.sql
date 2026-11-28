use supermarket;

select vendor, drink_id, quantity from orders;

-- group by
select vendor, drink_id, sum(quantity) AS total_per_vendor FROM orders GROUP BY vendor

;

-- PARTITION BY
SELECT 	vendor, drink_id, quantity,
		sum(quantity) OVER (PARTITION BY vendor) AS total_per_vendor
        FROM orders;
        
-- transactions
select * from drink;

START TRANSACTION;
-- 1 buena
UPDATE drink
SET is_available = FALSE where id = 1; 
-- 2 buena 
UPDATE drink
SET is_available = TRUE where id = 2;
-- 3 mala
UPDATE drink
SET is_availables = FALSE where id = 100;

COMMIT;        
SELECT * from drink;

ROLLBACK;
SELECT * from drink;