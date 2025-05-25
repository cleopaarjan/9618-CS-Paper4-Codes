#DECLARE DataArray:ARRAY[0:24] OF INTEGER
DataArray=[]

try:
    file=open("Data.txt","r")
    for x in range(25):
        filedata=int(file.readline().strip())
        DataArray.append(filedata)
    file.close()
except IOError:
    print("File Dosent Exist")

def PrintArray(IntegerArray):
    outputline=""
    for x in range(25):
        outputline=outputline+str(IntegerArray[x])+" "
    print(outputline) 


PrintArray(DataArray)

def LinearSearch(IntegerArray,SearchValue):
    count=0
    for x in range(25):
        if IntegerArray[x]==SearchValue:
            count+=1
    return count
Flag=False
while Flag==False:
    num=int(input("ENter the number between 0 and 100: "))
    if num>=0 and num<=100:

        Flag=True

tempcount=LinearSearch(DataArray,num)
print("the number",num,"is found",tempcount,"times")

