import json
def inventory():
    try:
        x = {"Inventorydata": []} #Create a dictionary containing key as Inventorydata and value as a list
        n = int(input('Enter the number of inventory objects-'))
        for i in range(n):
            y = {} #for every value of i create a dictionary and append it to the list in dict
            y['name'] = input('Enter the name-')
            y['Weight'] = int(input("Enter the weight-"))
            y['Price'] = int(input('Enter the amount-'))
            x["Inventorydata"].append(y)

        #print(x)
        with open('invent.json', 'w') as fp: #write the dict to the json file
            json.dump(x,fp)


        with open('invent.json', 'r') as fp: #Read the json file
            data = json.load(fp)

        for i in range(n): #Print the data from the json file
            a=data["Inventorydata"][i]["name"] #this variable stores value of the key 'Name'
            b=data["Inventorydata"][i]["Weight"] #variable b stores the value of the key 'Weight'
            c=data["Inventorydata"][i]["Price"] #variable c stores the value of the key
            d=(b*c) #calculation of total cost
            print('Name-',a,'Total Cost-',d)

    except:
        print('Error!')

inventory()

