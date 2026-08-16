# POSTGRES GUIDE FOR THE ANXIOUS DEV

- **installation guide**: [blue-ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04)

NOte: it is not necessary to run the prerequisite steps on the local laptop. Creating a user and adding prmissions is needed when deploying on servers.

### Login as postgres user (created automatically at install)

```
sudo -i -u postgres
psql
```

### Connect to working database

```
\c inventar_db

SELECT * FROM inventory_table;
```

Trebuie pus ; la final mereu ca altfel comanda ramane activa.



