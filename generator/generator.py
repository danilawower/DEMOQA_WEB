import random

from data.data import Person
from faker import Faker  # библиотека для данных

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():  # вызываем класс Пёрсон из даты с определёнными полями
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name(),
        email=faker_ru.email(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),  #рандомное число от 10 до 80
        salary=random.randint(10, 80),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )
