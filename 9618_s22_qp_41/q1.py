#DECLARE FileData:ARRAY
FileData=[[""]*2 for x in range(11)]

def ReadHighScore():
    File=open("HighScore.txt","r")
    for x in range(0,10):
        FileData[x][0]=File.readline().strip()
        FileData[x][1]=File.readline().strip()
    File.close()

def OutputHighScores():
    for x in range(0,11):
        combine=FileData[x][0] + " "+str(FileData[x][1])
        print(combine)



def Arrange(Username,Score):
    for x in range(0,10):
        if int(Score) >int(FileData[x][1]):
            
            Temp1=FileData[x][0]
            Temp2=FileData[x][1]
            FileData[x][0]=Username
            FileData[x][1]=Score
            count=x+1
            while count<10:
                second1=FileData[count][0]
                second2=FileData[count][1]
                FileData[count][0]=Temp1
                FileData[count][1]=Temp2

                Temp2=second1
                Temp2=second2
                count=count+1
            break

print("Before")
ReadHighScore()
OutputHighScores()

userflag=False
while userflag==False:
    Username=input("ENTER YOUR USERNAME: ")
    if len(Username)==3:
        userflag=True



scoreflag=False
while scoreflag==False:
    Score=input("Enter the score: ")
    if int(Score)>1 and int(Score)<100000:
        scoreflag=True

Arrange(Username,Score)
print("After")
OutputHighScores()
def WriteTopTen():
    file=open("NewHighScore.txt","w")
    for x in range(0,10):
        file.write(str(FileData[x][0])+ "\n")
        file.write(str(FileData[x][1]+"\n"))
    file.close()
    