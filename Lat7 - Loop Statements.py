#kelipatan 5
#angka 5, 10, 15, 20, 25 
# for i in range(5, 30, 5):
#     print(i)


# for i in range(10):
#     print("Looping!")

#contoh soal: angka kelipatan 3, tapi stop di 21
# for i in range(3, 50, 3):
#     if i == 21:
#         break

#     print(i)

#contoh soal: Print angka ganjil dari 1 sampai 10
# for i in range(1, 11):
#     #skip semua angka genap
#     if i % 2 == 0:
#         continue

#     print(i)

# #contoh soal: Print angka ganjil dari 1 sampai 10
# for i in range(1, 11):
#     #Jika dia tidak habis di bagi 2
#     if i % 2 != 0:
#         continue

#     print(i)


uang =100
while(uang > 0):
    print("Masih punya uang: " + str(uang))
    uang -= 10 #uang = uang - 10

print("Uang sudah habis")
