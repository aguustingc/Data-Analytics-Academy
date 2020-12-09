import pandas as pd
import sqlite3

conexion = sqlite3.connect('sakila.db')
df=pd.read_sql('SELECT DISTINCT title, description FROM film_list LIMIT 7', conexion)

print(df.head(3))