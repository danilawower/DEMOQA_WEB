import dataclasses


@dataclasses.dataclass
class Person:
    full_name: str = None                  #строковые данные
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None