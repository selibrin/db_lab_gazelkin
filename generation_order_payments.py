import psycopg2
import random

connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="15062001",
    host="127.0.0.1",
    port="5432"
)
connection.autocommit = True


select_payments_SQL = "SELECT payment_id FROM payments"
select_orders_SQL = "SELECT order_id FROM orders"

with connection.cursor() as cursor:
    cursor.execute(select_payments_SQL)
    rows_payments_raw = cursor.fetchall()

    cursor.execute(select_orders_SQL)
    rows_orders_raw = cursor.fetchall()

payments = list(map(lambda s: s[0], rows_payments_raw))
orders = list(map(lambda s: s[0], rows_orders_raw))



def random_connection():
    km = random.randint(5, 300)
    _order = random.choice(orders)
    _payment = random.choice(payments)
    _tuple = (km, _payment, _order)
    return _tuple


insert_orders_payments_SQL = "INSERT INTO order_payments (order_payment_km, order_payment_payment_id, " \
                             "order_payment_order_id) VALUES (%s, %s, %s)"

with connection.cursor() as cursor:
    for order in orders:
        cursor.execute(insert_orders_payments_SQL, random_connection())


connection.close()
