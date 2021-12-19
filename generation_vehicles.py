import psycopg2
import random
import datetime
from pandas.core.common import flatten


def random_datetime(start_date=datetime.date(2020, 12, 30),
                    end_date=datetime.date(2021, 12, 30)):
    return random.random() * (end_date - start_date) + start_date


connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="15062001",
    host="127.0.0.1",
    port="5432"
)
connection.autocommit = True

region_digits_list = []
with open("C:/Users/selib/Desktop/db_txt/region_digits.txt", encoding='utf-8') as f:
    for line in f:
        fileline = line.replace(',', '')
        try:
            region_digits_list.append([int(x) for x in fileline.split()])
        except (Exception,):
            pass


def flatten(l1):
    return [item for sublist in l1 for item in sublist]


serie_list = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']

registration_number_list = ['00' + str(n) for n in range(1000)]
registration_number_list = list(map(lambda s: s[len(s) - 3:len(s) + 1], registration_number_list))


def random_plate():
    plate = random.choice(serie_list) + random.choice(registration_number_list) + random.choice(serie_list) + \
            random.choice(serie_list) + str(random.choice(flatten(region_digits_list)))

    return plate


SQL = "INSERT INTO vehicles (vehicle_id, vehicle_maintenance_date) VALUES (%s, %s)"

with connection.cursor() as cursor:
    for i in range(301):
        cursor.execute(SQL, (random_plate(), random_datetime(),))

connection.close()
