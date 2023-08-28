import dataclasses



@dataclasses.dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
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
    color_name: list = None



@dataclasses.dataclass
class Subject:
    subject_name: list = None
