# list = [-21, -1, -31, 1, 4, 34,99]
#
# b = sorted(list)
#
# i = int(input("nhap vao 1 so: "))
# if i not in b:
#     print("not found")
# else:
#     for index, i in enumerate(b):
#         print("found {0} at {1}".format(i, index))
#         break

numbers = [-21, -1, -31, 1, 4, 34,99]
x = int(input("nhap vao 1 so: "))
found_index = -1

for index, number in enumerate(numbers):
     if x == number:

         found_index = index
         break

if found_index == -1:
    print("not found")
else:
    print("found: ", found_index)
