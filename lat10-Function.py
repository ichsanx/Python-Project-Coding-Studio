# # Create and call
# def greet():
#     print("Hello Stranger!")
#     print("Nice To Meet You")
# greet()
# greet()


# #passing argument
# #Parameter = name, age
# def greet(name, age):
#     print("name: " + name)
#     print("age: " + str(age))
# #Argumenr = "Budi", 20
# greet("Budi", 20)




# def add5(number):
#     total = number + 5
#     return total
# number = 10
# number_added_5 = add5(number)
# print (number_added_5)

#lambda Fumction
number = 10
total = lambda n: n+5
print(total(number))