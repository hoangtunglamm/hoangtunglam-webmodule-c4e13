prices={'banana':4,'apple':2,'orange':1.5,'pear':3}
stock={'banana':6,'apple':0,'orange':32,'pear':15}

for fruit in prices:
    print(fruit)
    print("prices: {}".format(prices[fruit]))
    print("stock: {}".format(stock[fruit]))

total = 0
for fruit in prices:
    print("Price of {0} is {1}$".format(fruit, prices[fruit] * stock[fruit]))
    total += (prices[fruit] * stock[fruit])
print("Total value:$",total)
