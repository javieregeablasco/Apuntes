use supermarket;

select * from drink;

-- if
DELIMITER $$
CREATE PROCEDURE review_stock (
	IN quantity INT, 
    IN quantity_2 INT
)

BEGIN
	IF quantity > 100 AND quantity_2 > 75 THEN
		SELECT 'Stock alto';
	ELSEIF quantity BETWEEN 50 AND 100 AND quantity_2 BETWEEN 25 and 75 THEN
		SELECT 'Stock normal';
	ELSE 
		SELECT 'Stock bajo';
       END IF;    
END$$
DELIMITER ;
 
call review_stock(120,50);

-- borrar procedure
DROP PROCEDURE IF EXISTS review_stock;

-- if ternario
SELECT 
	name,
	IF(is_available = True, 'disponible','no disponible') AS Estado_disponibilidad 
FROM drink;


DELIMITER $$
CREATE PROCEDURE revisar_stock (IN my_drink_id INT)
BEGIN
	DECLARE available BOOL;
    SELECT is_available INTO available FROM drink WHERE id=my_drink_id;
	
    IF available THEN
		SELECT concat(my_drink_id, ' Disponible') AS 'Estado disponibilidad';
    ELSE 
		SELECT concat(my_drink_id, 'No disponible') AS 'Estado disponibilidad' ;
    END IF;    
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS revisar_stock;
call revisar_stock(3);

DELIMITER $$
CREATE PROCEDURE count_to_five()
BEGIN
	DECLARE i int DEFAULT 1;
    
    WHILE i <=5 DO
		SELECT concat('Número', i) AS 'Valor bucle';
        SET i = i+1;
    END WHILE;    
    

END$$

DELIMITER ;

CALL count_to_five();

DROP PROCEDURE IF EXISTS count_to_five; 

DELIMITER $$
CREATE PROCEDURE llenar_tabla()
BEGIN
	DECLARE i int DEFAULT 1;
       
    WHILE i <=5 DO
		INSERT INTO orders (vendor, drink_id, quantity)
        VALUES (concat('Prueba', i), 1, rand(i)*100);
        SET i = i+1;
    END WHILE;    
END$$

DELIMITER ;

CALL llenar_tabla();

DROP PROCEDURE IF EXISTS llenar_tabla; 

SELECT * FROM orders;

SELECT RAND(100),
        RAND(),
        RAND();