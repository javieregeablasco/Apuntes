USE bbdd_3;

-- update siempre va acompañado de un where, sino se actualizarán todos los registros de la tabla
update clientes set ciudad = 'Madrid' where ciudad = 'Barcelona';

