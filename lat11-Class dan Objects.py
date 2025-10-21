# class angka:
#     jumlah = 5

# a = angka()
# print(a.jumlah)


# #custome value
# class person:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
# p1 = person("Cecep", 20, 95)
# p2 = person("Andi", 33, 90)

# print(p1.__dict__)
# print(p2.__dict__)





# #menambahakan greet ke custome value/ function di dalam class
# class person:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
    
#     def greet(self):
#         print("Halo, " + self.name + "!")

# p1 = person("Cecep", 20, 95)
# p2 = person("Andi", 33, 90)

# # print(p1.__dict__)
# # print(p2.__dict__)

# p1.greet()
# p2.greet()




#menambahakan greet ke custome value/ function di dalam class
class animal: #parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("Hello!")

class cat(animal): #child class
    def __init__(self, name, age, colour, weigh):
        super().__init__(name, age)
        self.colour = colour
        self.weight = weigh

class dog(animal): #child class
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type