import psycopg2
import random
import datetime


def random_datetime(dt=datetime.datetime(2021, 1, 30)):
    start_date = dt
    end_date = datetime.datetime(2021, 12, 30)
    start_datetime = random.random() * (end_date - start_date) + start_date
    end_datetime = start_datetime + random.random() * datetime.timedelta(hours=8)

    return start_datetime.replace(second=0, microsecond=0), end_datetime.replace(second=0, microsecond=0)


connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="15062001",
    host="127.0.0.1",
    port="5432"
)
connection.autocommit = True


selectSQL = "SELECT porter_id FROM porters"
with connection.cursor() as cursor:
    cursor.execute(selectSQL)
    rows_raw = cursor.fetchall()
rows = [row_raw[0] for row_raw in rows_raw]

worktime_list = []
for i in range(len(rows)):
    for j in range(21):
        while True:
            start, end = random_datetime()
            tmp_list = worktime_list[i:i + j + 1][0:2]
            if tmp_list.count(start) == 0 and tmp_list.count(end) == 0:
                worktime_list.append((start, end, i+1))
                break

insertSQL = "INSERT INTO schedules (schedules_datetime_start, schedules_datetime_end, schedules_porter_id) " \
         "VALUES (%s, %s, %s)"


with connection.cursor() as cursor:
    for worktime in worktime_list:
        cursor.execute(insertSQL, worktime)


connection.close()
