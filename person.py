import traceback
from log import Log
class Person:

    def __init__(self, name, lastname, age) -> None:
        self.name=name
        self.lastname=lastname
        self.age = age
        Log("CRE", "Создан объект класса Person")

    def __str__(self):
        s = f"Имя и Фамилия: {self.name} {self.lastname}, Возраст: {self.age} \nНомер: {self.number}"
        return s
