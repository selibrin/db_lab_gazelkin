import psycopg2
import numpy as np
import random

connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="15062001",
    host="127.0.0.1",
    port="5432"
)

connection.autocommit = True

k_list = np.linspace(40, 150, num=150)

price_per_km = [float(random.choice(k_list)) for _ in range(150)]
loading_price = [500 + 30 * i for i in range(150)]
area_ratio = [1 + random.random() for _ in range(150)]
time_ratio = [1 + random.random() for _ in range(150)]

pseudo_tuples = [[price_per_km[i], loading_price[i], area_ratio[i], time_ratio[i]] for i in range(150)]

SQL = "INSERT INTO payments (payment_price_per_km, payment_loading_price, payment_area_ratio, payment_time_ratio) " \
      "VALUES (%s, %s, %s, %s)"

with connection.cursor() as cursor:
    for pseudo_tuple in pseudo_tuples:
        cursor.execute(SQL, pseudo_tuple)


connection.close()
