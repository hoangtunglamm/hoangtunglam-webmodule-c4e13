a = open("alice.txt", "r").read()
b = a.lower()
e = ",.[]();''\\\"?!-"
for i in e:
    b = b.replace(i, " ")
c = b.split(sep=None, maxsplit=-1)
c.sort()

for j in c:

    count = 0
    for k in range(len(c)):
        if c[k] == j:
            count += 1
    if count > 0:
        print(j, count)
        #em quy`, print no trong vong lap, k biet cho ra the nao T_T
