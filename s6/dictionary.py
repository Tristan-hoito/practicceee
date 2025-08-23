<<<<<<< HEAD
# userinfo = {
#     "full_name": "Tristan Ragasa",
#     "age" : 17,
#     "address" : "Marilao"
# }

person = dict(name="pogi", age=17, address="Marilao")
# print("")
# print(userinfo)
# print("")

# print("")
# print(person["name"])
# print(userinfo["full_name"])
# print("")

# print(userinfo.get("age"))

# person = {
#     "full_name" : input("Input your name: "),
#     "age" : input(int("Input your age: ")),
#     "address" : input("Input your address: ")
# }

# person.get("weight")
# person_weight = person.get("weight")

# person["email"] = "tristanpogi@gmail.com"
# person["email"] =(input("enter email: "))

# person.update({"email": input("Input your new Email: ")})

# person.pop("email")
# #removes email
# del person["age"]

# person.clear()

# print(person)

user = {"name": "Tristan",
        "age":17, 
        "pogiba":"POGI",
        "friends":[
            {"name": "Mark"},
            {"name": "Lorenz"},
            {"name": "Zac"},
            {"name": "Reynald"}
                   ]
        }

for key in user.keys():
    pass

for value in user.values():
    pass

for key,value in user.items():
=======
# userinfo = {
#     "full_name": "Tristan Ragasa",
#     "age" : 17,
#     "address" : "Marilao"
# }

person = dict(name="pogi", age=17, address="Marilao")
# print("")
# print(userinfo)
# print("")

# print("")
# print(person["name"])
# print(userinfo["full_name"])
# print("")

# print(userinfo.get("age"))

# person = {
#     "full_name" : input("Input your name: "),
#     "age" : input(int("Input your age: ")),
#     "address" : input("Input your address: ")
# }

# person.get("weight")
# person_weight = person.get("weight")

# person["email"] = "tristanpogi@gmail.com"
# person["email"] =(input("enter email: "))

# person.update({"email": input("Input your new Email: ")})

# person.pop("email")
# #removes email
# del person["age"]

# person.clear()

# print(person)

user = {"name": "Tristan",
        "age":17, 
        "pogiba":"POGI",
        "friends":[
            {"name": "Mark"},
            {"name": "Lorenz"},
            {"name": "Zac"},
            {"name": "Reynald"}
                   ]
        }

for key in user.keys():
    pass

for value in user.values():
    pass

for key,value in user.items():
>>>>>>> 408d95c61bd0c38a7969be3a2e927603899568ee
    print(f"{key}: {value}")