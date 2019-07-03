import json


x={"Inventorydata":[ ]}
n=int(input('Enter the number of inventory objects-'))
y={ }
for i in range(n):
    y['name'] = input("Enter the Name-")
    y['Weight'] = int(input("Enter the weight-"))
    y['Price']=int(input('Enter the amount-'))
    x["Inventorydata"].append(y)
print(x)