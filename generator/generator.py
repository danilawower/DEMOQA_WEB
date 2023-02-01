import random

from data.data import Person, Color, Date
from faker import Faker  # библиотека для данных

faker_ru = Faker('ru_RU')
fake_en = Faker('en')
Faker.seed()


def generated_person():  # вызываем класс Пёрсон из даты с определёнными полями
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name(),
        email=faker_ru.email(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),  # рандомное число от 10 до 80
        salary=random.randint(10, 80),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn()
        # (Mobile Subscriber Integrated Services Digital Number) — номер мобильного абонента цифровой сети с интеграцией служб для связи в стандартах GSM, UMTS
    )


def generated_file():
    path = rf'C:\Users\daniil\PycharmProjects\automation_qa_course\filetest{random.randint(0, 999)}.txt'  # путь к файлу и его название
    file = open(path, 'w+')  # открыть файл
    file.write(f'Hello World{random.randint(9, 222)}')
    file.close()
    return file.name, path  # возвращаем имя созданного файла и путь к нему


def generated_color():
    yield Color(
        color_name=['Red', 'Green', 'Yellow', 'Purple']
    )


def generated_date():
    yield Date(
        year=fake_en.year(),
        month=fake_en.month_name(),
        day=fake_en.day_of_month(),
        time="12:00",
    )