class Person:
    def __init__(self,name,age,gender,interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests
    def hello(self):
        print("Hello My name is" + " " + self.name + " "+"and i am "+" "+ self.age +""+"years old my interests are"+" "+self.interests)

person = Person("Ryan", "30", "male", "being a hardorse, agile and ssd hard")
person.hello()

