def IterativeVowels(Value):
    Total=0
    LengthString=len(Value) 
    for x in range(0,LengthString):
        FirstCharacter=Value[0]
        if FirstCharacter=="a" or FirstCharacter=="e" or FirstCharacter=="i" or FirstCharacter=="o" or FirstCharacter=="u":
            Total=Total+1
        Value=Value[1:len(Value)]
    return Total

temp=IterativeVowels("house")
print("Iterative",temp) 

def RecursiveVowels(Value):
    if len(Value)==0:
        return 0
    else:
        FirstCharacter=Value[0]
        if FirstCharacter=="a" or FirstCharacter=="e" or FirstCharacter=="i" or FirstCharacter=="o" or FirstCharacter=="u":
            Value=Value[1:len(Value)]
            return 1+RecursiveVowels(Value)
        else:
            Value=Value[1:len(Value)]
            return 0 + RecursiveVowels(Value)

temp2=RecursiveVowels("imagine")
print("Recursive",temp2)