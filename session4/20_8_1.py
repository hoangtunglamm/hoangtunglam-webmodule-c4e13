import string
alphabet = list(string.ascii_lowercase)
a = input("wirte something: ")
b = list(a)

for i in alphabet:
    count = 0
    for j in range(len(b)):
        if b[j].lower() == i:
            count += 1
    if count > 0 :
        print(i, count)
