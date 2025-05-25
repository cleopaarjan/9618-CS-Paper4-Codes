filedata=[[""]*2 for x in range(11)] #string

def ReadHighScores():
    filename="HighScore.txt"
    file=open(filename,"r")
    for x in range(10):
        filedata[x][0]=file.readline().strip()
        filedata[x][1]=file.readline().strip()
    file.close
ReadHighScores()

def OutputHighScores (): 
   for x in range(0, 11): 
       Output = filedata[x][0] + " " + filedata[x][1] 
       print(Output) 

OutputHighScores()

name=input("enter the name : ")
while len(name)!=3:
    name=input("enter the name : ")
score=int(input("score:"))
while score>=1 and score<=10000:    
    score=int(input("score:"))

def Arrange(username,scoree):
    for x in range(0,10):
        if scoree>filedata[x][1]:
            Temp1=filedata[x][0]
            temp2=filedata[x][1]
            filedata[x][0]=username
            filedata[x][1]=score
            count=x+1
            while count<10:
                second1=filedata[count][0]
                second2=filedata[count][1]
                filedata[count][0]=Temp1
                filedata[count][1]=temp2
                Temp1=second1
                temp2=second2

ReadHighScores()
OutputHighScores()
Arrange(name,score)
OutputHighScores()

def WriteTopTen():
    Filename="NewHighScore.txt"
    file=open(Filename,"w")
    for x in range(10):
        file.write(str(filedata[x][0])+'\n')
        file.write(str(filedata[x][1])+'\n')
        file.close