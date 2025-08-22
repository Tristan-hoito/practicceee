class GradeSystem:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def get_grade(self):
        print(self.__grade)
        return self.__grade
    
    def set_grade(self, new_grade):

        print("")
        # new_grade = int(input("Please put your new grade: "))
        print("")

        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            print("")
            print(f"Your grade is: {self.__grade}")
            print("")
            return
        
        else:
            print("Bobo bawal yan")
            print("")
            exit()
            

student1 = GradeSystem ("Tristan")
student1.set_grade(100)
student1.get_grade()
print("")

# print(student1.get_grade())
# print("")

