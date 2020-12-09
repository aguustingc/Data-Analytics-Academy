import sqlite3

conexion=sqlite3.connect('sakila.db')
cursor=conexion.cursor()
cursor=conexion.execute('SELECT DISTINCT title, description FROM film_list LIMIT 7')

for fila in cursor:
    print(fila)