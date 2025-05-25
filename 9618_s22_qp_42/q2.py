import random 
#DECLARE ArrayData:ARRAY[0:9,0:9] OF INTEGER

ArrayData=[[0]*10 for x in range(10)]

for x in range(0,10):
    for y in range(0,10):
        ArrayData[x][y]=random.randint(1,100)
ArrayLength=10


def PrintArray():
    for x in range(0,10):
        for y in range(0,10):
            print(ArrayData[x][y]," ",end='')
        print("")


ArrayLength=10
for x in range(0,ArrayLength):
    for y in range(0,ArrayLength-1):
        for z in range(0,ArrayLength-y-1):
            if ArrayData[x][z]>ArrayData[x][z+1]:
                TempValue=ArrayData[x][z]
                ArrayData[x][z+1]=TempValue

print("Before")
PrintArray()

def BinarySearch(SearchArray,Lower,Upper,SearchValue):
    if Upper>=0:
        Mid=(Lower+(Upper-1))//2
        if SearchArray[0][Mid]==SearchValue:
            return Mid
        elif SearchArray[0][Mid]>SearchValue:
            return BinarySearch(SearchArray,Lower,Mid-1,SearchValue)
        else:
            return BinarySearch(SearchArray,Mid+1,Upper,SearchValue)
        return-1

print("After")
PrintArray()

firstcheck=int(input("Enter the number: "))
secondcheck=int(input("Enter the number: "))
print(BinarySearch(firstcheck))
print(BinarySearch(secondcheck))


 

