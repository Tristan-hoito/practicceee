<<<<<<< HEAD
info = {}

def contacts():
    name = input("Please input your name: ")
    number = input("Please input your number: ")

    info["name"] = name
    info["number"] = number

    return info

#read
def read(): 
    print("")
    print(info.get("name"))
    print(info.get("number"))

    return info

#update
def update():
    info.update({"name" : input("Please enter your new name: ")})
    info.update({"number" : input("Please enter your new number: ")})

    return info

#delete
def delete():
    info.clear()

    return info

def malupit():
    while True:
        
        print("")
        print("1. Add")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        print("")
        i = input("Please choose 1-5: ")

        if i == "1":
            contacts()
            continue

        elif i == "2":
            read()
            continue

        elif i == "3":
            update()
            continue

        elif i == "4":
            delete()
            continue

        elif i == "5":
            exit()

        else:
            print('Invalid Input, please choose 1-4')
            continue

=======
info = {}

def contacts():
    name = input("Please input your name: ")
    number = input("Please input your number: ")

    info["name"] = name
    info["number"] = number

    return info

#read
def read(): 
    print("")
    print(info.get("name"))
    print(info.get("number"))

    return info

#update
def update():
    info.update({"name" : input("Please enter your new name: ")})
    info.update({"number" : input("Please enter your new number: ")})

    return info

#delete
def delete():
    info.clear()

    return info

def malupit():
    while True:
        
        print("")
        print("1. Add")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        print("")
        i = input("Please choose 1-5: ")

        if i == "1":
            contacts()
            continue

        elif i == "2":
            read()
            continue

        elif i == "3":
            update()
            continue

        elif i == "4":
            delete()
            continue

        elif i == "5":
            exit()

        else:
            print('Invalid Input, please choose 1-4')
            continue

>>>>>>> 408d95c61bd0c38a7969be3a2e927603899568ee
malupit()