DataArray=[] #25 elements integer
try:
    filename="Data.txt"
    file=open(filename,"r")
    line=file.readline().strip()
    while line !="":
        DataArray.append(int(line))
        line=file.readline().strip()
    file.close()

except IOError:
    print("file not found")


def PrintArray(DataArrayP):
    output=""
    for x in range(len(DataArrayP)): 
        output=output+str(DataArrayP[x])+" "
    print(output)

PrintArray(DataArray)



def linearSearch(dataARRAYP,searchkey):
    count=0
    for a in range(len(dataARRAYP)):
        if dataARRAYP[a]==searchkey:
            count+=1
    return count
searchkey=int(input("Enter a number between 0 and 100 inclusive: "))
while searchkey<0 or searchkey>100:
    searchkey=int(input("Enter a number between 0 and 100 inclusive: "))
x=linearSearch(DataArray,searchkey)
print("the number",searchkey,"is found",x,"times.")    
