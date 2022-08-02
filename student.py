import traceback
from person import Person
from log import Log
class Student(Person):
    def __init__(self, name, lastname, age, number): 
        Person.__init__(self, name, lastname, age)
        self.number=number
        self.gradebook={}
        Log("CRE", "Создан объект класса Student")

    def new_mark(self, discipline, mark):
        self.gradebook[discipline]=mark
        Log("INF", "Добавлена новая оценка")

    def delete_mark(self,discipline,mark):
        try:
            del self.gradebook[discipline]
        except:
            print("Нет такого предмета в списке")
            Log("ERR", "ОШИБКА - Такой предмет отсутствует")


    def __getitem__(self, discipline):
        return self.gradebook[discipline]

    def __str__(self):
        s = f"Имя и Фамилия: {self.name} {self.lastname}, Возраст: {self.age} \n\nСтудентческий номер: {self.number} \n{self.gradebook}\n"
        return s
