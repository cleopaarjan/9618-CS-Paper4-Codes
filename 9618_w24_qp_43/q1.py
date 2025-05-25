Strings=[]
def ReadData():
    
    Filename="Data.txt"
    file=open(Filename,"r")
    for x in range(45):
        Strings.append(file.readline().strip())
    return Strings
        

def FormattedArray(strings):
    concat=""
    for a in range(len(strings)):
         concat= concat+" "+strings[a]
    return concat

y=ReadData()
x=FormattedArray(Strings)
print(x)

def CompareString(String1,String2):
    if String1>String2:
        return 1
    elif String2>String1:
        return 2 
def Bubble(sstrings):
    for b in range(len(sstrings)):
        for a in range(len(sstrings)-1):
            if CompareString(sstrings[a],sstrings[a+1])==1:
                sstrings[a],sstrings[a+1]=sstrings[a+1],sstrings[a]
    return sstrings

p=Bubble(Strings)
print(p)
e=FormattedArray(Strings)
print(e)