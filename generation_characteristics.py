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

type_of_delivery_list = ['Перевозка вещей', 'Перевозка стройматериалов', 'Перевозка оборудования', 'Перевозка мебели',
                         'Перевозка дивана', 'Перевозка пианино', 'Перевозка лодок и катеров', 'Перевозка мотоцикла',
                         'Перевозка кабеля', 'Перевозка леса', 'Перевозка пиломатериалов', 'Автомобильные перевозки',
                         'Переезд магазина', 'Квартирный переезд', 'Дачный переезд', 'Офисный переезд',
                         'Доставка грузов', 'Рефрижераторные перевозки', 'Перевозка контейнеров',
                         'Перевозки крупногабаритных грузов', 'Перевозка по области']

lifting_capacity_list = ['1500', '2000', '3000', '5000', '7500', '10000', '15000', '20000']

marque_and_model_list = []
with open("/Users/selibrin/Downloads/marks.txt", encoding='utf-8') as f:
    for line in f:
        try:
            marque_and_model_list.append(line.replace(';', ' ')[0:len(line) - 1])

        except (Exception,):
            pass

selectSQL = "SELECT vehicle_id FROM vehicles"
with connection.cursor() as cursor:
    cursor.execute(selectSQL)
    rows_raw = cursor.fetchall()
rows = [row_raw[0] for row_raw in rows_raw]

insertSQL = "INSERT INTO characteristics (characteristic_type_of_delivery," \
            "characteristic_lifting_capacity, characteristic_marque_and_model," \
            "characteristic_vehicle_id) VALUES (%s, %s, %s, %s)"

with connection.cursor() as cursor:
    for i in range(len(rows)):
        marque_and_model = random.choice(marque_and_model_list)

        if i % 7 == 0:
            cursor.execute(insertSQL, (random.choice(type_of_delivery_list), random.choice(lifting_capacity_list),
                                       marque_and_model, rows[i],))

        if i % 28 == 0:
            cursor.execute(insertSQL, (random.choice(type_of_delivery_list), random.choice(lifting_capacity_list),
                                       marque_and_model, rows[i],))

        if i % 17 == 0:
            cursor.execute(insertSQL, (random.choice(type_of_delivery_list), random.choice(lifting_capacity_list),
                                       marque_and_model, rows[i],))

        cursor.execute(insertSQL, (random.choice(type_of_delivery_list), random.choice(lifting_capacity_list),
                                   marque_and_model, rows[i],))

connection.close()
