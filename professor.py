import traceback
from person import Person
from log import Log

class Professor(Person):

    def __init__(self, name, lastname, age, number, post):
        Person.__init__(self, name, lastname, age)
        self.number=number
        self.post=post
        self.disciplines=[]
        Log("CRE", "Создан объект класса Teacher")

    def change(self, post):
        self.post=post
        Log("INF", "Изменение должности")

    def __add__(self, other):
        self.disciplines += other
        Log("INF", "Добавление дисциплины")

    def delete(self, other):
        self.disciplines.remove(other)
        Log("INF", "Удален список дисциплин")

    def __str__(self):
        s = f"Имя и Фамилия: {self.name} {self.lastname}, Возраст: {self.age} \nНомер: {self.number} \nPost: {self.post}"
        return s
 
