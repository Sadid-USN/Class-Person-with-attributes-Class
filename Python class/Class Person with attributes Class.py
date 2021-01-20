class Person:
    people_count = 0
    def __init__(self, name, surname, placeOfBirth,yearOfBirth ):
        self.name = name
        self.surname = surname
        self.placeOfBirth = placeOfBirth
        self.yearOfBirth = yearOfBirth
        Person.people_count += 1

    def information(self, n):
        for i in range(n):
            print(f"Name: {self.name}, Surname: {self.surname}, PlactOfBirth: {self.placeOfBirth}, yearOfBirth {self.yearOfBirth}")
    def getAge(self, currentYear):
                print(f"Age: {currentYear - self.yearOfBirth}")


p1 = Person("Sadid", "Idibekov", "Tajikistan", 1988)
p2 = Person("Kobe", "Bryant", "USA", 1978)
p3 = Person("Ilon", "Musk", "USA", 1971)
p1.test = "hello"


p1.information(1)
p2.information(1)
p3.information(1)
p3.getAge(2021)