# students = ["nhieza","krisha","ras","blessie","jacob"]
# students.append("tristan")
# students.insert(0, "rayquaza")
# students.remove("ras")
# students.pop() #remove last name
# students.sort() #sort alphabetically, if int (0,1,2,3)
# students.reverse() #reverse array order

# print(students)


# def find_student(array):

#     names = input("Enter the name of the student: ")

#     for student in array:
#         if student == names:
#             print(f"Laro {student} nahanap.")
#             return

#     print(f"diko mahanap {names}")

# find_student(students)

def manage_cart():
    cart = []

    ### add item in array
    def add_item(array):

        ###count how many items to add
        def count():
            while True:
                try:
                    count = int(input("How many items do you want to add in cart?: "))
                    return count
                except ValueError:
                    print('Invalid input')
        #######

        while True:
            try:
                print(cart)
                item_number = count()

                if not cart:
                    for i in range(item_number):
                        item = input(f"{i+1}. Input item name: ")
                        array.append(item)
                        print(array)

                    return
                
                if len(cart) > 0:
                    def index_item():
                        while True:
                            index = int(input(f"Where do you want to put the grocery item? 0-{len(cart)}: "))
                            if index > len(cart):
                                print("Invalid input")
                                continue
                            return index
                        
                    index = index_item()

                    # def find_existing_item(existing_name):
                    #     for item_name in cart:
                    #         if item_name == existing_name:
                    #             print("Item already exist")
                    #             break
                    #     return

                    for i in range(item_number):
                        item = input(f'{i+1}. Input item name: ')
                        array.insert(index,item)

                return
            except ValueError:
                print("Please enter an item name")
                continue
    ###########

    # def edit_item():


    def menu():
        while True:
            
            print("1. Add an item to the cart")
            print("2. Edit an item in the cart")
            print("3. View an item in the cart")
            print("4. Remove an item in the cart")
            print("5. Exit")

            try:
                choice = int(input("Enter number from 1-5: "))
                if choice == 1:
                    add_item(cart)
                    pass
                elif choice == 2:
                    #edit_item(cart)
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    pass
                elif choice == 5:
                    print("Exiting app.....")
                    exit()

            except ValueError:
                print("Please enter a number 1-5")
                continue
    menu()

    add_item(cart)
        
manage_cart()
