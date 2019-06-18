import os
fn=input('Enter the file name-')
if(not os.path.isfile(fn)):
    f=open(fn,'w')
    data=input=input('Enter data to write-')
    f.write(data+'\n')
    print('Data Written')
    f.close()
else:
    print('file does not exists!')





