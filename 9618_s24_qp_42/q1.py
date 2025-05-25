#q1{a,b}
WordArray=[]
answers=0
aws=input("ENTER easy/medium/hard: ")
aws=aws[0].upper()+aws[1:].lower()+".txt"

def ReadWords(pasy):
    global answers
    file1 = open(pasy,"r")
    for y in range(14):
        x=file1.readline().strip()
        WordArray.append(x)  
    answers=len(WordArray)-1
    #print(answers,WordArray) 
ReadWords(aws)

# *procedure bolse tai no returns
# *no printing cause bole na
#c{i}
def Play():
    #print(WordArray[0],answers)

    countCorrect = 0
    
    while True:
        userInput = input("Enter a word: ")
        if userInput=="no":
            break

        for loc in range(1,len(WordArray)):
            if userInput == WordArray[loc]:
                print("Answer \""+userInput+"\" is correct")
                countCorrect += 1
                WordArray[loc] = None
                break    
    p=countCorrect/answers*100
    print("percantage: ",round(p,2),"%")
    unused=[]
    #c{ii}
    for ii in range(1,14):
        if WordArray[ii]!=None:
            unused.append(WordArray[ii])  
    print("Unusedwords-",unused)
    
#print(WordArray)  #initial array
Play()
#print(WordArray) # none none lekha array

