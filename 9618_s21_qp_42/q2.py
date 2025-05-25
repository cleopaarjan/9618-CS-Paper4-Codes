arrayData=[10,5,6,7,1,12,13,15,21,8]

def linearsearch(searchkey):
    for x in range(len(arrayData)):
        if arrayData[x]==searchkey:
            return True
        else :
            return False
        
searchkeyp=int(input("enter a number: "))
x=linearsearch(searchkeyp)
if x==True:
    print("found! ")
else:
    print("not found")

def bubbleSort(arrayDatap):
    for x in range(0,len(arrayDatap)):
        for y in range(0,len(arrayDatap)-1):
            if arrayDatap[y]<arrayDatap[y+1]:
                temp=arrayDatap[y]
                arrayDatap[y]=arrayDatap[y+1]
                arrayDatap[y+1]=temp
    
xx=bubbleSort(arrayData)
print(arrayData)