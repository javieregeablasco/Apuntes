→ revisar el codigo
 



normalizacion de tablas.
  evitar duplicados.
  evitar redundantes.   


instalar workbench para acceso BBDD
instalar xamp para servidor BBDD

crear bbdd

# youtubers

-- pendientes --




pildoras
https://www.youtube.com/watch?v=yZk9NdxFUrk&list=PLU8oAlHdN5Bmx-LChV4K3MbHrpZKefNwn&index=4

-- completados --

soy dalto
https://www.youtube.com/watch?v=DFg1V-rO6Pg

boluda
https://www.youtube.com/watch?v=8N4M994IDt8&list=PLQxX2eiEaqbx5EoP7GDA8sMBMV84hRcLM

AMazaing Code → muy bueno
https://youtu.be/Fk45d7J0p6o?

sergi code:
https://www.youtube.com/watch?v=Fca_kWJJXvo

moure dev
https://www.youtube.com/watch?v=OuJerKzV5T0

# documentos de referencia

w3schools.com/sql/sql_datatypes.asp

# repositorios para recursos

https://github.com/mouredev/hello-sql
https://github.com/sergiecode/curso-sql-desde-cero

# clientes gratuitos

dbeaver
workbench → cliente nativo de mysql
devart
dbforge
tableplus →

# Guía de Uso de Comillas en SQL

En SQL, el uso de las comillas simples (`' '`), las comillas dobles (`" "`) y las comillas invertidas o *backticks* (`` ` ` ``) es uno de los temas que más confusión causa, ya que su comportamiento varía según el motor de base de datos que estés utilizando (MySQL, PostgreSQL, SQL Server, etc.).

---

## 1. Comillas Simples (`'text'`) ➔ Para TEXTO y FECHAS

Es el **estándar universal** en SQL. Se utilizan exclusivamente para delimitar **literales de cadena** (strings) y valores de fecha/hora.

* **Cuándo usarlas:** Siempre que vayas a introducir un texto, un email, una fecha, etc.
* **Ejemplo:**

```sql
SELECT * FROM clientes WHERE name = 'Juan' AND fecha_alta = '2026-06-02';
```

## 2. Comillas Dobles ("objeto") ➔ Para Identificadores Estándar

Según el estándar ANSI SQL, las comillas dobles se utilizan para identificadores (nombres de tablas, columnas o bases de datos), especialmente cuando estos nombres contienen espacios, caracteres especiales o coinciden con palabras reservadas del sistema.

* Cuándo usarlas: Si tu columna se llama igual que una función de SQL (como Date o Select) o si tiene espacios (aunque tener espacios es una mala práctica).

* Ejemplo:

```SQL
SELECT "first name", "order date" FROM "lista de pedidos";
```

* Soporte: Es el estándar en PostgreSQL, Oracle y SQLite.

* Nota sobre SQL Server: En lugar de comillas dobles, SQL Server prefiere los corchetes: [first name].

## 3. Comillas Invertidas (`objeto`) ➔ El "Capricho" de MySQL / MariaDB

Las comillas invertidas (backticks) no son estándar de SQL, pero son extremadamente populares porque MySQL y MariaDB las usan para el mismo propósito que las comillas dobles en otros sistemas: proteger nombres de tablas y columnas.

* Cuándo usarlas: En MySQL, para envolver nombres de tablas o columnas que puedan causar conflicto o que contengan caracteres especiales.

* Ejemplo:

```SQL
CREATE TABLE `clientes` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `select` VARCHAR(255)  -- 'select' es palabra reservada, los backticks la salvan
);
```
