# count = int(input("Enter a number: "))

# while count <= 10:
#     if count % 2 == 0:
#         print(f"Count Even: {count}")
#     else:
#         print(f"Count Odd: {count}")

#     count += 1

#---

# while True:
#     if count > 10:
#         break
#     else:
#         print(f'Poging number: {count}')
    
#     count += 1

# while True??:
#     if count > 10:
#         if count % 2 == 0:
#             print(f'Count: {count}')
#             continue

#     count += 1

#     if count > 100:
#         break

# for i in range(0,10,2):
#     print(i)

# for i in range(10):
#     if i == 9:
#         break
#     print(i)

# for i in range(100):
#     if i % 2 == 0:
#         continue
#     elif i == 51:
#         break

#     print(i)

fruits = ['Apple', 'Strawberry', 'Banana']
# #0,1,2
# print(fruits[1])

for i in range(len(fruits)):
    print(f"Basket {i + 1} contains: {fruits[i]}")

for i in range(len(fruits)):
    if fruits[i] == 'Banana':
        continue
    print(f"Basket {i + 1} contains: {fruits[i]}")