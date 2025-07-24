def calculator(operation, value1, value2):
    try:
        if operation != '+' or operation != '-' or operation != '*' or operation != '/':
            print("Invalid Operation")
    
        value1 = int(value1)
        value2 = int(value2)

        if operation == "+":
            print (f"The total sum is:  {value1 + value2}")
            return value1 + value2
        elif operation == "-":
            print (f"The total difference is: {value1 - value2}")
            return value1 - value2
        elif operation == "*":
            print (f"The total difference is: {value1 * value2}")
            return value1 * value2
        elif operation == "/":
            print (f"The total difference is: {value1 / value2}")
            return value1 / value2
        else:
            print('Syntax Error')

    except ValueError:
        print("Invalid Input: Please enter a whole number")
    
calculated_number = calculator(
    input("Enter Operation: "),
    input('Enter 1st Number: '),
    input("Enter 2nd Number: ")
)