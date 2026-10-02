use supermarket;

DELIMITER $$
	CREATE PROCEDURE count_loop()
    BEGIN
		DECLARE i INT DEFAULT 1;
        
		bucle: LOOP
			SELECT CONCAT('Número: ',i) AS 'Valor del bucle';
			SET i = i+1;
        
			If i>5 THEN LEAVE BUCLE;
            END IF;
        END LOOP;    
    END$$
    

DELIMITER ;

DROP PROCEDURE IF EXISTS count_loop;

CALL count_loop();