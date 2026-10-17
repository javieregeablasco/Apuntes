USE bbdd_3;

SELECT avg(age) FROM clientes;
SELECT avg(age) FROM clientes where ciudad = 'Madrid';
SELECT avg(age) FROM clientes where ciudad in ('Madrid', 'Barcelona');
SELECT avg(age) FROM clientes where age in between 20 and 30;