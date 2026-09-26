create schema if not exists bbdd_3;
drop schema if exists bbdd_3 cascade;

drop table if exists clientes cascade;
create table clientes (
    id int primary key auto_increment,
    name varchar(255) not null,
    age int not null,
    ciudad varchar(255) not null,
    constraint 'mayor de edad' as 'Comprobar edad' check (age > 0 and age < 120)
);

insert into clientes (name, age, ciudad) values ('Juan', 25, 'Madrid');
insert into clientes (name, age, ciudad) values ('Maria', 30, 'Barcelona');
insert into clientes (name, age, ciudad) values ('Pedro', 35, 'Madrid');
insert into clientes (name, age, ciudad) values ('Ana', 28, 'Barcelona');
insert into clientes (name, age, ciudad) values ('Luis', 22, 'Madrid');
insert into clientes (name, age, ciudad) values ('Sofia', 27, 'Barcelona'); 
insert into clientes (name, age, ciudad) values ('Carlos', 31, 'Madrid');
insert into clientes (name, age, ciudad) values ('Laura', 29, 'Barcelona');
insert into clientes (name, age, ciudad) values ('Jorge', 26, 'Madrid');
insert into clientes (name, age, ciudad) values ('Marta', 24, 'Barcelona'); 
insert into clientes (name, age, ciudad) values ('Diego', 32, 'Madrid');
insert into clientes (name, age, ciudad) values ('Lucia', 27, 'Barcelona');
insert into clientes (name, age, ciudad) values ('Alberto', 29, 'Madrid');
insert into clientes (name, age, ciudad) values ('Sara', 26, 'Barcelona');  
insert into clientes (name, age, ciudad) values ('Andres', 30, 'Madrid');
insert into clientes (name, age, ciudad) values ('Isabel', 28, 'Barcelona');
insert into clientes (name, age, ciudad) values ('Fernando', 27, 'Madrid');
insert into clientes (name, age, ciudad) values ('Carmen', 25, 'Barcelona');
insert into clientes (name, age, ciudad) values ('Rafael', 31, 'Madrid'); 
insert into clientes (name, age, ciudad) values ('Elena', 29, 'Barcelona');
insert into clientes (name, age, ciudad) values ('Sergio', 26, 'Madrid');
insert into clientes (name, age, ciudad) values ('Patricia', 28, 'Barcelona');
insert into clientes (name, age, ciudad) values ('Javier', 30, 'Madrid');
insert into clientes (name, age, ciudad) values ('Miriam', 27, 'Barcelona');
insert into clientes (name, age, ciudad) values ('Oscar', 29, 'Madrid');
insert into clientes (name, age, ciudad) values ('Vanessa', 26, 'Barcelona');

