import psycopg2
import random


def fullnames():
    f = open('C:/Users/selib/Desktop/db_txt/fullnames2.txt', 'r', encoding='utf-8')
    fullname_list = f.readlines()
    f.close()
    return fullname_list


connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="15062001",
    host="127.0.0.1",
    port="5432"
)
connection.autocommit = True

list_fio = fullnames()
ability_to_drive_list = [bool(random.randint(0, 1)) for _ in range(len(list_fio))]

SQL = "INSERT INTO porters (porter_ability_to_drive, porter_fullname) VALUES (%s, %s)"

with connection.cursor() as cursor:
    for i in range(len(list_fio)):
        cursor.execute(SQL, (ability_to_drive_list[i], list_fio[i],))


connection.close()
