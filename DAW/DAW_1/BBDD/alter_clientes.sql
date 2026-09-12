use alumnos;
alter table clientes change column name nombre varchar(20);

select * from clientes;
describe clientes;

alter table clientes modify column nombre varchar(22); 

alter table clientes add apellidos varchar(255) not null default('Pedro');
alter table clientes drop column apellidos;

