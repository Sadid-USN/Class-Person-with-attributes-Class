class Person:
    people_count = 0
    def __init__(self, name, surname, placeOfBirth,yearOfBirth ):
        self.name = name
        self.surname = surname
        self.placeOfBirth = placeOfBirth
        self.yearOfBirth = yearOfBirth
        Person.people_count += 1

    def information(self):
        print(f"Name: {self.name}, Surname: {self.surname}, PlactOfBirth: {self.placeOfBirth}, yearOfBirth {self.yearOfBirth}")

    def getAge(self,):
        currentYear = 2021
        print(f"Age:  {self.name} = {currentYear - self.yearOfBirth}")


p1 = Person("Sadid", "Idibekov", "Tajikistan", 1988)
p2 = Person("Michael ", "Jordan", "USA", 1963)
p3 = Person("Ilon", "Musk", "USA", 1971)



p1.information()
p2.information()
p3.information()
p1.getAge()
p2.getAge()
p3.getAge()
