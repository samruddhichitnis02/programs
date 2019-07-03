import json
def management():
    try:
        with open('management.json', 'r') as fp:
            data = json.load(fp) #load is used to decode the data from the json file

        for i in range(3):
            a=data["Inventorydata"][i]["Name"] #this variable stores value of the key 'Name'
            b=data["Inventorydata"][i]["Weight"] #variable b stores the value of the key 'Weight'
            c=data["Inventorydata"][i]["Price per Kg"] #variable c stores the value of the key
            d=(b*c) #calculation of total cost
            print('Name-',a,'Total Cost-',d)

    except:
        print('File not Found!')

management()