from Stos import Stos
from Student import Student

# stos = Stos(2)
# stos.push(2)
# stos.push(3)
# stos.push(4)
# print(stos)
# print("pop: ", stos.pop())
# print(stos)
# print("pop: ", stos.pop())
# print(stos)
# print("pop: ", stos.pop())
# print(stos)
# print("pop: ", stos.pop())
# print(stos)

student = Student(email="adamski@gmail.com", name="adam", surname="adamski")

print(repr(student))

student = Student(email="adamski@gmail.com", name="adam", surname="zadamski")
student2 = Student(email="babacki@gmail.com", name="bob", surname="bobowski")

print(Student.compareStudentsName(student,student2))
print(Student.compareStudentsSurname(student,student2))

def alphabeticGreater(x,y,func):
    return func(x,y)

alphabeticGreater(student, student2, Student.compareStudentsName)
alphabeticGreater(student, student2, Student.compareStudentsSurname)

# email,name,surname = student.getPersonalData()
# print(email,name,surname)




#-----------------------------------------------------------------------
#Zadanie 1
#-----------------------------------------------------------------------

class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        current = self.head
        output = []
        while current:
            output.append(str(current.data))
            current = current.nextE
        return " - ".join(output)

    def get(self, e):
        current = self.head
        prev = None
        while current:
            if current.data == e:
                if prev:
                    prev.nextE = current.nextE
                    if current == self.tail:
                        self.tail = prev
                else:
                    self.head = current.nextE
                    if not current.nextE:
                        self.tail = None
                self.size -= 1
                return True
            prev = current
            current = current.nextE
        return False

    def append(self, e, func = None):
        new_element = Element(e)
        if self.head is None:
            self.head = new_element
            self.tail = new_element
            self.size += 1
            return
        if func is None:
            func = lambda x, y: x >= y
        current = self.head
        prev = None
        while current:
            if func(current.data, e):
                if func(current.data, e):
                    if prev:
                        prev.nextE = new_element
                    else:
                        self.head = new_element
                    new_element.nextE = current
                    self.self += 1
                    return
                prev = current
                current = current.nextE
            self.tail.nextE = new_element
            self.tail = new_element
            self.size += 1