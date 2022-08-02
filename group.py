"""
Создать класс Group.
    Поля: номер группы, список группы (список экземпляров класса Student), преподаватель-куратор (экземпляр класса Professor). Определить конструктор.
    Переопределить метод преобразования в строку для печати всей информации о группе (с использованием переопределения в классах Professor и Student).

    Переопределить методы
    получения количества студентов функцией len,
    получения студента/преподавателя по индексу,
    изменения по индексу,
    удаления по индексу (0 индекс - преподаватель, начиная с 1 - студенты).
                    
    Переопределить операции + и - для добавления или удаления студента из группы.
    Добавить функцию создания txt-файла и записи всей информации в него (в том числе зачетной книжки студентов).
"""
import traceback
from student import Student
from professor import Professor
from log import Log

class Group:
    def __init__(self, numberg, students, professors):
        self.numberg=numberg
        self.students=students
        self.professors = professors
        Log("CRE", "Создан объект класса Group")

    def __str__(self):
        a = f"Group: {self.numberg}\n\nStudents:\n\n"
        for i in range(len(self.students)):
            a+= (self.students[i].__str__()+"\n")
            
        a+= "Professors:\n\n"
        for i in range(len(self.professors)):
            a+= (self.professors[i].__str__()+"\n\n")
        return a
    
    def len(self):
        return len(self.students)

    def __getitem__(self, index):
        return self.students[index]
    

    def __delitem__(self, index):
        if index:
            del self.students[index - 1]
            Log("INF", "Удаление по индексу стундента")
        else:
            del self.professors
            Log("INF", "Удаление по индексу препода")

    def __setitem__(self, index, name):
        if key:
            self.students[index - 1] = name
        else:
            self.professors = name

    def __add__(self, student):
        self.students
        self.students.append(student)
        Log("INF", "Удаление студента из списка")

    def __sub__(self, student):
        for i in range(len(students)):
            if students[i]==student:
                del students[i]
                Log("INF", "Удаление студента из списка")

    def delete_student(self, numb):
        try:
            del self.students[numb-1]
        except:
            print("Нет такого студента в группе")
            Log("ERR", "ОШИБКА - Такого студента нет")

    def txt(self):
        name = "File.txt"

        with open(name, "w",encoding="utf-8") as f:
            Log("CRE", "Открытие текстового файла")
            f.write(Group.__str__(self))
            f.close()
            

            
        
        

    

    

    
