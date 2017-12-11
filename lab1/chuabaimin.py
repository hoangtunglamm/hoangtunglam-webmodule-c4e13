number = [-21, -1, -31, 1, 4, 34,99]

min_number = number[0]

for index, number in enumerate(number):
    if min_number > number :
        min_number = number
print("min: ", min_number)        
