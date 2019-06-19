# Exploring Data Using Metabase

## MySQL:

- Install mysql:

```
sudo apt-get install mysql-server
```

- Inicializa o SGBD (mysql):

```
systemctl start mysql
```

- Access mysql:

```
sudo mysql -u root -p
```

- Executing SQL script;

```
sudo mysql -u root -p  < 00_create_database_and_table.sql
```

## Process table and generate sql insert script to feed database:

```
python generate_sql_insert_eleicoes_data.py [table] [sql_name_file]
```

## Load data to MySQL:

```
sudo mysql -u root < 01_insert_eleicoes_data.sql
```

## Executing Metabase:

```
Follow instructions on the [metabase website.](https://metabase.com)

java -jar metabase.jar
```