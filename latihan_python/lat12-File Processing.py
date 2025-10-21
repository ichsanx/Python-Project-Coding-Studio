# #open file "read"
# file = open(r"C:\Users\hp\Downloads\Python Kursus Project\lat12_proses\coding-studio_example proses.txt", "r")
# print(file.read())

# #replace isi file "write"
# file = open(r"C:\Users\hp\Downloads\Python Kursus Project\lat12_proses\coding-studio_example proses.txt", "w")
# file.write("Ini adalah text yang baru")
# file.close()

# #tambahkan isi file "append"
# file = open(r"C:\Users\hp\Downloads\Python Kursus Project\lat12_proses\coding-studio_example proses.txt", "a")
# file.write(", Ini adalah text yang baru cuy")
# file.close()

#tambahkan isi file "dengan append"
file = open(r"C:\Users\hp\Downloads\Python Kursus Project\lat12_proses\coding-studio_example proses.txt", "a")
file.write("\n, Ini adalah text yang baru cuy di append dengan enter")
file.close()