import dataclasses


@dataclasses.dataclass
class Person:
    full_name: str = None                  #строковые данные
    email: str = None
    current_address: str = None
    permanent_address: str = None