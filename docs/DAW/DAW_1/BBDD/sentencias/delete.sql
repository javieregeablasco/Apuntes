USE bbdd_3;

delete from clientes where id = 1;
delete from clientes where ciudad = 'Madrid';
delete from clientes where ciudad in ('Madrid', 'Barcelona');
delete from clientes where age in between 20 and 30;