use alumnos;

drop trigger if exists tg_email;

delimiter //
create trigger tg_email
after update on clientes
for each row
begin 
	if OLD.ciudad <> NEW.ciudad then
		insert into ciudad_history(ciudad_id, name)
		VALUES (old.id, OLD.ciudad);
	end if;
end//;

delimiter ;

update clientes set ciudad = 'Marsella' where id=1;

show triggers;
-- show tables;
SHOW CREATE TRIGGER tg_email;
SHOW CREATE TABLE clientes;
select database();