import random


from data.data import Person, Color, Subject
from faker import Faker


faker_ru = Faker('ru_RU')
fake_en = Faker('en')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name(),
        email=faker_ru.email(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10, 80),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
        index=random.randint(10, 20),
        country=faker_ru.country(),
        city=faker_ru.city()

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




def generated_subject():
    yield Subject(
        subject_name=['Math', 'Physics', 'English', 'Chemistry']
    )
