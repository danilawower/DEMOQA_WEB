import dataclasses




@dataclasses.dataclass
class Person:
    full_name: str = None  # строковые данные
    firstname: str = None
    lastname: str = None
    age: int = None  # числовые
    salary: int = None
    department: str = None
    email: str = None
    index: int = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None
    country: str = None
    city: str = None


@dataclasses.dataclass
class Color:
    color_name: list = None  # список


@dataclasses.dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None


@dataclasses.dataclass
class Car:
    car_name: list = None


@dataclasses.dataclass
class Website:
    site_type: list = None


@dataclasses.dataclass
class City:
    city_name: list = None


@dataclasses.dataclass
class Subject:
    subject_name: list = None
