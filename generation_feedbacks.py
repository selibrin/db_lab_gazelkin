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


texts_9_10 = ['Всё отлично', 'Хорошо', 'Четко, без накладок', 'Замечательно', 'Мне все понравилось',
              'Аккуратный грузщик', 'Отличный персонал', 'Очень быстро и удобно', 'Дешево и надежно',
              'Отличный сервис за отличную цену', 'Всем доволен, спасибо', 'Всем советую',
              'Бережный и аккуратный водитель, все супер', 'Достойный сервис', 'Лучшие среди конкурентов',
              'Молодцы!', 'Перевезли аккуратно и быстро', 'Годно']

texts_6_8 = ['Хорошо', 'Нормально', 'Прилично', 'Приличный сервис', 'Хорошие грузчики', 'Хороший водитель',
             'Вполне недурно', 'Порядочный сервис', 'Добротный сервис', 'Качественно и вполне недолго',
             'Добропорядочный персонал', 'Грузчики не халтурили, всё очень неплохо',
             'Достойный сервис, за достойные деньги', 'Очень похвально', 'Славненько']

texts_4_5 = ['Неплохо', 'Можно было и лучше', 'Ну, скажем, удовлетворительно', 'Сойдет',
             'Посредственный сервис, но для единственного раза сойдет', 'Куда ни шло', 'Сносно',
             'Очень и очень средний сервис...', 'Работу грузчиков оцениваю как вполне терпимую',
             'Средненький сервис за соответсвующую цену, ни больше ни меньше']

texts_0_3 = ['Ужасно', 'Плохо', 'Отвратительно', 'Чрезвычайно халтурный сервис', 'Скверный сервис',
             'Дикие мартышки, а не грузчики', 'Водитель видимо купил права, все ужасно', 'Хамы и лодыри',
             'Понабрали обезьян, груз пострадал', 'Это беспредел, весь груз побили и нахамили', 'Невыносимо',
             'Надо бы прикрыть эту безнадежную конторку']


def random_text(grade=10):
    if grade > 8:
        return random.choice(texts_9_10)
    elif grade > 5:
        return random.choice(texts_6_8)
    elif grade > 3:
        return random.choice(texts_4_5)
    elif grade > -1:
        return random.choice(texts_0_3)


select_orders_SQL = "SELECT order_id FROM orders WHERE order_status = 'Выполнен'"
insertSQL = "INSERT INTO feedbacks (feedback_order_id, feedback_text, feedback_grade) VALUES (%s, %s, %s)"
with connection.cursor() as cursor:
    cursor.execute(select_orders_SQL)
    rows_orders_raw = cursor.fetchall()
    rows_orders = list(map(lambda s: s[0], rows_orders_raw))

    for row in rows_orders:
        k = random.randint(0, 10)
        if (int(row) + k) % 7 != 0:
            cursor.execute(insertSQL, (row, random_text(k), k,))


connection.close()

