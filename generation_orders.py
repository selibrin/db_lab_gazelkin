import psycopg2
import random
import datetime

connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="15062001",
    host="127.0.0.1",
    port="5432"
)
connection.autocommit = True


def random_datetime(dtend=datetime.datetime(2021, 1, 30)):
    start_date = dtend
    end_date = datetime.datetime(2021, 12, 30)

    return random.random() * (end_date - start_date) + start_date


city_list = []
with open("C:/Users/selib/Desktop/db_txt/city.txt") as f:
    for line in f:
        try:
            city_list.append(line[:len(line) - 1])
        except (Exception,):
            pass

street_list = []
with open("C:/Users/selib/Desktop/db_txt/STREET.txt") as f:
    for line in f:
        try:
            if len(line.split(sep="\t")[0]) > 5:
                street_list.append(line.split(sep="\t")[0])
        except (Exception,):
            pass


def random_address():
    address = random.choice(city_list) + ', ул. ' + random.choice(street_list) + ', дом ' + \
              str(random.randint(1, 50)) + ', кв. ' + str(random.randint(1, 300))
    return address


select_customers_SQL = "SELECT customer_id FROM customers"
select_vehicle_SQL = "SELECT vehicle_id FROM vehicles"
select_porter_SQL = "SELECT porter_id FROM porters"
with connection.cursor() as cursor:
    cursor.execute(select_customers_SQL)
    rows_customers_raw = cursor.fetchall()

    cursor.execute(select_vehicle_SQL)
    rows_vehicles_raw = cursor.fetchall()

    cursor.execute(select_porter_SQL)
    rows_porters_raw = cursor.fetchall()
rows_customers = list(map(lambda s: s[0], rows_customers_raw))
rows_vehicles = list(map(lambda s: s[0], rows_vehicles_raw))
rows_porters = list(map(lambda s: s[0], rows_porters_raw))

insertSQL = "INSERT INTO orders (order_address_start, order_address_finish, " \
            "order_weight, order_delivery_time_start, order_delivery_time_interval, order_status, order_customer_id," \
            " order_vehicle_id, order_porter_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

check_list = [50 * i for i in range(1, 13)]
check_list2 = [39 * i for i in range(1, 17)]

order_list = []
for i in range(601):
    if i in check_list:
        dt = datetime.datetime(2021, 12, 30)
        k = 'Выполняется'
    else:
        dt = random_datetime()
        if i in check_list2:
            k = 'Отменен'
        else:
            k = 'Выполнен'
    order_list.append((random_address(), random_address(), random.randint(100, 1000), dt,
                       random.randint(1, 13), k, random.choice(rows_customers), random.choice(rows_vehicles),
                       random.choice(rows_porters)))

with connection.cursor() as cursor:
    for order in order_list:
        cursor.execute(insertSQL, order)

connection.close()
