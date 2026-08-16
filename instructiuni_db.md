### Creare user admin pentru baza de date inventar

```
daria@Daria-Katana-17-B13VFK:~$ sudo -u postgres createuser --interactive
Enter name of role to add: inventar_admin
Shall the new role be a superuser? (y/n) y
```

Sau putem folosi sql direct. Cream un user cu privilegii mai putine

```
postgres=# CREATE ROLE inventar_user WITH LOGIN PASSWORD 'student';
CREATE ROLE
postgres=# GRANT inventar_user CREATEDB;
ERROR:  syntax error at or near "CREATEDB"
LINE 1: GRANT inventar_user CREATEDB;
                            ^
postgres=# ALTER USER inventar_user CREATEDB;
ALTER ROLE
postgres=# ALTER USER inventar_user LOGIN

```

Baza de date o cream in userul postgres si setam permisiuni de acces de acolo [docs](https://www.postgresql.org/docs/8.0/sql-createdatabase.html)

```
CREATE DATABASE inventory_database
```