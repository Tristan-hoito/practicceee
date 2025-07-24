def age_converter(current_year, birth_year):
    try:
        current_year = len(int(current_year))
        birth_year = len(int(birth_year))

        if len != 4:
            print("The numbers should just be 4!")

        age = current_year - birth_year
        print(F"Your current age is: {age}")
        return current_year - birth_year

    except ValueError:
        print("Syntax Error")

age_converter(
    input("Input the current year today: "),
    input("Input your birth year: ")
)