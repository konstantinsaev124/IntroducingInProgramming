class Person():
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
    # def print_person(self):
    #     print(self.name)
    #     print(self.family)
    #     print(self.age)
    #     print(self.nationality)

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofgraduate):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofgraduate = yearofgraduate
    # def print_person(self):
    #     print(f"First name: {self.name} \n Last name: {self.family} \n Age: {self.age} \n Nationality: {self.nationality} \n Year of graduation: {self.yearofgraduate} \n University: {self.university}")

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, experience):
        super().__init__(name, family, age, nationality)
        self.experience = experience
    def print_person(self):
        print(f"First name: {self.name} \n Last name: {self.family} \n Age: {self.age} \n Nationality: {self.nationality} \n  Experience: {self.experience}")
  

ivan = Lecturer("Ivan", "Ivanov", 36, "Bulgarian", "5 godini")

ivan.print_person()