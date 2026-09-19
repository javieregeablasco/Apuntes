USE bbdd_3;
 
SELECT * FROM clientes where email like '%@gmail.com' or age between 20 and 30 limit 5 order by age desc;
