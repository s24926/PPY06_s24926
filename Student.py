class Student:
    def __init__(self, email, name, surname, all_grade=None, status=None):
        if all_grade is None:
            self.all_grade = {
            "project": -1,
            "l_1": -1,
            "l_2": -1,
            "l_3": -1,
            "h_1": -1,
            "h_2": -1,
            "h_3": -1,
            "h_4": -1,
            "h_5": -1,
            "h_6": -1,
            "h_7": -1,
            "h_8": -1,
            "h_9": -1,
            "h_10": -1,
            "grade": -1,
            }
        else:
            self.all_grade = all_grade

        self.email = email
        self.name = name
        self.surname = surname
        if status is None:
            self.status = None
        else:
            self.status = status

    def __str__(self):
        return self.email + " " + self.name + " " + self.surname + " " + str(self.all_grade) + " "+ str(self.status)

    def __repr__(self):
        return f"Student(email='{self.email}', name='{self.name}', surname='{self.surname}" \
               f"', all_grade={self.all_grade}, status={self.status})"
        #return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.email == other.email

    @staticmethod
    def compareStudentsName(x,y):
        return x.name >= y.name

    @staticmethod
    def compareStudentsSurname(x,y):
        return x.surname >= y.surname

    # def getPersonalData(self):
    #