global DataStored #integer 
global NumberItems #Integer 20 items 
DataStored=[]


def Initialise():
    global NumberItems
    global DataStored    

    NumberItems=int(input("how many numbers you want?"))
    if NumberItems>=1 and NumberItems<=20:
        for a in range(NumberItems):
            DataStored.append(int(input("number: ")))
        
    else:
        while NumberItems<1 or NumberItems>20:
            NumberItems=int(input("how many numbers you want?"))
        for a in range(NumberItems):
            DataStored.append(int(input("number: ")))

NumberItems=0
Initialise()
print(DataStored)
def bubbleSort():
    global NumberItems
    global DataStored

    for b in range(len(DataStored)):
        for a in range(len(DataStored)-1):
            if DataStored[a]>DataStored[a+1]:
                DataStored[a],DataStored[a+1]=DataStored[a+1],DataStored[a]

bubbleSort()
print(DataStored)

def BinarySearch(DataStored, DataToFind):
    begin_index = 0
    end_index = len(DataStored) - 1

    while begin_index <= end_index:
        midpoint = (begin_index + end_index) // 2
        midpoint_value = DataStored[midpoint]

        if midpoint_value == DataToFind:
            print("Found")
            return midpoint
        elif DataToFind < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1

    print("NOT FOUND")
    return -1

print(BinarySearch(DataStored, 2))  
