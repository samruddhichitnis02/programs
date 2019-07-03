import re
def expression():
    try:
        with open('regular', 'r') as f:
            data=f.read()
        name=input('Enter Your Name-') #Take the user name from user
        x=re.sub("<name>",name,data) #repalce <name> with name
        fname=input('Enter Your full name-') #Take the fullname from user
        y=re.sub("<full name>",fname,x) #replace <full name> with fname
        cno=input('Enter your contact number-') #Take the contact no from user
        z=re.sub("91-xxxxxxxxxx",cno,y) #replace  91-xxxxxxxxxx with cno
        date1=input('Enter the date-') # Take the date from user
        a=re.sub("01/01/2016",date1,z) #replace 01/01/2016 with date1
        print(a)
        change=input('Type c to Change your specifications-') #tell the user to enter c if they wish to cahnge any specification
        if(change=='c'):
            choice=int(input('Enter 1 to change the name, 2 to change the full name,3 to change the contact number, 4 to change the date-')) # tell the user to press any no from 1-4 to change any of the specification
            if(choice==1):
                name1=input('Enter your name-')
                y1=re.sub(name,name1,a)
                print(y1)
            elif(choice==2):
                fname1=input('Enter the full name-')
                y2=re.sub(fname,fname1,a)
                print(y2)
            elif(choice==3):
                cno1=input('Enter the contact no-')
                y3=re.sub(cno,cno1,a)
                print(y3)
            elif(choice==4):
                date=input('Enter the date in X/XX/XXXX format-')
                y4=re.sub(date1,date,a)
                print(y4)
            else:
                print('Invalid Choice!')
    except:
        print('Check the file name or check the input you have given!')


expression()
