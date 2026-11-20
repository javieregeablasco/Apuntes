use alumnos;
--    create table dni(
-- 	  dni_id int AUTO_INCREMENT primary key,
--    dni_number int not null,
--    user_id int,
--    unique(dni_number),
--    FOREIGN KEY(user_id) references clientes(id)
-- );
    
create table companyas(
	company_id int AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(25) NOT NULL
);
	
create table ciudad_history(
	ciudad_id int, 
    name VARCHAR(25) 
);
	
alter table ciudad_history ADD column id int auto_increment primary key;    
    
    
    