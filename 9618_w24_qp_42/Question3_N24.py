HighScores=[]
HighScores=[['' for x in range(3)]for y in range(7)]
def ReadData():
    Temp=[]
    try:
        File=open("HighScoreTable.txt")
        Temp=File.read().split("\n")
        File.close()
    except:
        print("No file found")
    NumberRecords=len(Temp)-1
    counter=0

def ReadData():
    Temp=[]
    HighScores=[]
    try:
        File=open("HighScoreTable.txt")
        Temp=File.read().split("\n")
        File.close()
    except:
        print("no file found")
    numberRecords=len(Temp)-1
    counter=0

    while counter<numberRecords:
        HighScores.append(Temp[counter],Temp[counter+1],Temp[counter+2],Temp[counter+3]) 
        counter+=3
    return HighScores

def OutputhighScores(HighScores):
    for x in range(len(HighScores)):
        print(HighScores)

def SortScores(HighScores):
    Counter=0
    ArrayLen=len(HighScores)

    for x in range(ArrayLen-1):
        for y in range(0,ArrayLen-x-1):
            if int(HighScores[y][1])<int(HighScores[y+1][1]):
                HighScores[y],HighScores[y+1]=HighScores[y+1],HighScores[y]
            elif int(HighScores[y][1]) == int(HighScores[y+1][1]): 
                if int(HighScores[y][2]) < int(HighScores[y+1][2]): 
                    HighScores[y], HighScores[y + 1] = HighScores[y + 1], HighScores[y] 
    return HighScores 

 
HighScores = [] 
HighScores = ReadData() 
print("Before") 
OutputhighScores(HighScores) 
HighScores = SortScores(HighScores) 
print("After") 
OutputhighScores(HighScores) 
