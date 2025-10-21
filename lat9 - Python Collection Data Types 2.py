# tupleExample = ('Python', 20, 3.8, True, 20)
# print(tupleExample)


# #Dictionary
# customer = {
#     "Nama": "Cecep",
#     "Umur": 30
# }

# # print(customer)
# print(customer["Nama"])
# print(customer["Umur"])



# #ganti nama
# customer = {
#     "Nama": "Cecep",
#     "Umur": 30
# }
# customer["Nama"] = "Dodi"

# print(customer["Nama"])
# print(customer["Umur"])


# #ADD/ Meambahakan
# customer = {
#     "Nama": "Cecep",
#     "Umur": 30
# }
# customer["Pekerjaan"] = "Programmer"

# print(customer)



# #Hapus pakai pop
# customer = {
#     "Nama": "Cecep",
#     "Umur": 30
# }
# customer["Pekerjaan"] = "Programmer"
# customer.pop("Umur")

# print(customer)



# #SET menambahaan penggabungan
# numbers1 = {1, 3, 5, 4, 10}
# numbers2 = {3, 4, 10, 7, 8}

# #{1, 3, 4, 5, 7, 8, 10}
# numbers_union = numbers1.union(numbers2)
# print(numbers_union)


# #Difference cari angka di baris 1 yang tidk ada di baris 2
# numbers1 = {1, 3, 5, 4, 10}
# numbers2 = {3, 4, 10, 7, 8}

# #{1, 5}
# diffeence1 = numbers1.difference(numbers2)
# print(diffeence1)


#Symetrix diffrence print yang tidak ada dikeduanya
# numbers1 = {1, 3, 5, 4, 10}
# numbers2 = {3, 4, 10, 7, 8}

# sym_diffrence = numbers1.symmetric_difference(numbers2)
# print(sym_diffrence)



#cari angka sama dari kedua memakai intersection
numbers1 = {1, 3, 5, 4, 10}
numbers2 = {3, 4, 10, 7, 8}

intersect = numbers1.intersection(numbers2)
print(intersect)
