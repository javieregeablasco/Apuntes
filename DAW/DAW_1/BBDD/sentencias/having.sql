USE bbdd_3;

SELECT * FROM clientes group by ciudad;
SELECT sum(age) FROM clientes group by ciudad;
SELECT count(age), age FROM clientes group by age;
SELECT count(age), age FROM clientes group by age having count(age) > 1 order by age desc;