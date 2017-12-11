a = [1,3,4,6,8,10,15,17]
x = int(input("nhao vao 1 so "))

start = 0
stop = len(a)
mid = (start +stop ) // 2
found_index = -1
while start <= stop:
    mid = (start +stop ) // 2
    if x == a[mid]:
        found_index = mid
        break
    elif x < a[mid]:
        stop = mid
        mid = (start +stop ) // 2
    else:
        start = mid
        mid = (start +stop +1 ) // 2
if found_index == -1:
    print("not found")
else:
    print("found at: ", found_index)
