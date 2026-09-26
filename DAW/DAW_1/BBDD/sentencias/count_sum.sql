USE bbdd_3;

select sum(age) from clientes;
select sum(age) from clientes where ciudad = 'Madrid';
select count(*) from clientes;
select count(*) from clientes where ciudad = 'Madrid';


