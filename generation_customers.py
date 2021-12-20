import psycopg2


def fullnames():
    f = open('C:/Users/selib/Desktop/db/db_txt/fullnames.txt', 'r', encoding='utf-8')
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

SQL = "INSERT INTO customers (customer_fullname) VALUES (%s)"

with connection.cursor() as cursor:
    for fullname in list_fio:
        cursor.execute(SQL, (fullname,))


connection.close()
