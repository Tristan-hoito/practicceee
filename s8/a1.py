class Person:
    def __init__(self, name, age, birthday, motto):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.motto = motto
    
    def pogi(self):
        print(f"Hello! My name is {self.name} and currently I am {self.age} years old.\nMy birthday is {self.birthday} and My motto in life is:\n {self.motto}")

person1 = Person("Tristan Ragasa",
                17,
                "September 17, 2007",
                "Living a life full of mistakes is much better than living a life full of regrets.")

print("")
person1.pogi()
print("")