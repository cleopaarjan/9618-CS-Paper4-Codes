#DECLARE DataArray[0:99] OF INTEGER
DataArray=[0]*100
def ReadFile():
    global DataArray
    try:
        File=open("IntegerData.txt","r")
        for x in range(0,100):

            temp=int(File.readline().strip())
            DataArray[x]=temp
    except IOError:
        print("File Not Found")

def FindValues():
    global DataArray

    flag=False
    while flag==False:
        Datatofind=int(input("Enter the Number: "))
        if Datatofind>1 and Datatofind<100:
            
            flag=True
            
            
            

    count=0
    for x in range(0,100):
        if DataArray[x]==Datatofind:
            count+=1

    return count


def BubbleSort():
    global DataArray
    for x in range(0,100):
        for y in range(0,99):
            if DataArray[y]>DataArray[y+1]:
                DataArray[y],DataArray[y+1]=DataArray[y+1],DataArray[y]
ReadFile()
numcount=FindValues()
print("The count of the number is: "+str(numcount))

BubbleSort()
#for x in range(100):
#    print(DataArray[x])
#DECLARE DataArray[0:99] OF INTEGER
DataArray=[0]*100
def ReadFile():
    global DataArray
    try:
        File=open("IntegerData.txt","r")
        for x in range(0,100):

            temp=int(File.readline().strip())
            DataArray[x]=temp
    except IOError:
        print("File Not Found")

def FindValues():
    global DataArray

    flag=False
    while flag==False:
        Datatofind=int(input("Enter the Number: "))
        if Datatofind>1 and Datatofind<100:
            flag=True

    count=0
    for x in range(0,100):
        if DataArray[x]==Datatofind:
            count+=1

    return count


def BubbleSort():
    global DataArray
    for x in range(0,100):
        for y in range(0,99):
            if DataArray[y]>DataArray[y+1]:
                DataArray[y],DataArray[y+1]=DataArray[y+1],DataArray[y]
ReadFile()
numcount=FindValues()
print("The count of the number is: "+str(numcount))

BubbleSort()
for x in range(100):
    print(DataArray[x])
