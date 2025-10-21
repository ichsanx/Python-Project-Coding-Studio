# append, insert
# remove, pop, del, clear
# list iteraction
# check if an item exists in list
# methods: len, copy, concat (+ dan extend), index, sort, reverse

# append, insert
# listExample = [42, 'Phython', 3.85, 50]
# listExample.insert(1, 'Data Science')
# listExample.append('Java Script')
# print(listExample)


# remove, pop, del, clear
# listExample = [42, 'Phython', 3.85, 50]
# print(listExample)
# listExample.remove('Phython')
# print(listExample)

# listExample = [42, 'Phython', 3.85, 50]
# print(listExample)
# listExample.pop()
# print(listExample)

# listExample = [42, 'Phython', 3.85, 50]
# print(listExample)
# del listExample[2]
# print(listExample)

# listExample = [42, 'Phython', 3.85, 50]
# print(listExample)
# listExample.clear()
# print(listExample)


# # list iteraction
# listExample = [40, 55, 20, 75, 80]
# for item in listExample:
#     print(item)

# listExample = [40, 55, 20, 75, 80]
# for item in listExample:
#     if item % 2 == 0:
#         print(item)



# # check if an item exists in list
# listExample = [40, 55, 20, 75, 80]
# if 40 in listExample:
#     print("Terdapat angka 40 di dalam listExample")



# # methods: len, copy, concat (+ dan extend), index, sort, reverse
# listExample = [40, 55, 20, 75, 80]
# listExample2 = listExample.copy()
# listExample2[0] = 100
# print(listExample)
# print(listExample2)

#concat
# listExample = [40, 55, 20]
# listExample2 = [70, 100]
# print(listExample+listExample2)

#+ dan extend
# listExample = [40, 55, 20]
# listExample2 = [70, 100]
# listExample.extend(listExample2)
# print(listExample)  

#index
# listExample = [40, 55, 20]
# print(listExample.index(55))

#sort
# listExample = [40, 55, 20]
# listExample.sort()
# print(listExample)

#reverse
listExample = [40, 55, 20]
listExample.reverse()
print(listExample)