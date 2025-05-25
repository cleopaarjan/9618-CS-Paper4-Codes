class Card():
    #PRIVATE Number : INTEGER
    #PRIVATE colour : STRING
    def __init__(self,NumberP,ColourP):
        self.__Number=NumberP
        self.__Colour=ColourP 
    def GetNumber(self):
            return self.__Number
    def GetColour(self):
        return self.__Colour

#DECLARE CardArray:ARRAY[0:29] OF Card  
CardArray=[0]*30
file=open("CardValues.txt","r")

for x in range(30):
    Numberread=int(file.readline().strip())
    Colourread=file.readline().strip()
    CardArray[x]=Card(Numberread,Colourread)
file.close()

NumberChosen=[False]*30

def Choosecard():
    global NumberChosen
    flag=True
    while flag==True:
        CardSelected=int(input("Selcetg a Card between 1 and 30: "))
        if CardSelected<1 or CardSelected >30:
            print("Number must be between 1 and 30")
        elif NumberChosen[CardSelected-1]==True:
            print("Already taken")
        else:
            print("Valid")
            flag=False

    NumberChosen[CardSelected-1]=True
    return CardSelected-1
#DECLARE Player1:ARRAY[0:3]
Player1=[]
for x in range(4):
    ReturnNumber=Choosecard()
    Player1.append(CardArray[ReturnNumber])

for x in range(4):
    print(Player1[x].GetNumber())
    print(Player1[x].GetColour())




        

