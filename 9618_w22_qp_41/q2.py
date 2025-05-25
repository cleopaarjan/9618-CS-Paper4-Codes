class card():
    #PRIVATE Number : INTEGER
    #PRIVATE Colour : STRING

    def __init__(self,NumberP,ColourP):
        self.__Number=NumberP
        self.__Colour=ColourP

    def GetColour(self):
        return self.__Colour
    def GetNumber(self):
        return self.__Number

class Hand():
    #PRIVATE Cards : ARRAY[0:9] OF CARD
    #PRIVATE Firstcard : INTEGER
    #PRIVATE NumberCards : INTEGER
    def __init__(self,card1,card2,card3,card4,card5):
        self.__FirstCard=0
        self.__NumberCards=5
        self.__Cards=[]
        self.__Cards.append(card1)
        self.__Cards.append(card2)
        self.__Cards.append(card3)
        self.__Cards.append(card4)
        self.__Cards.append(card5)

    def GetCard(self,index):
        return self.__Cards[index]

onered=card(1,"red")
twored=card(2,"red")
threered=card(3,"red")
fourred=card(4,"red")
fivered=card(5,"red")
oneblue=card(1,"blue")
twoblue=card(2,"blue")
threeeblue=card(3,"blue")
fourblue=card(4,"blue")
fiveblue=card(5,"blue")
oneyellow=card(1,"yellow")
twroyellow=card(2,"yellow")
threeyellow=card(3,"yellow")
fouryellow=card(4,"yellow")
fiveyellow=card(5,"yellow")

Player1=Hand(onered,twored,threered,fourred,oneyellow)
Player2=Hand(twroyellow,threeyellow,fouryellow,fiveyellow,oneblue)

def CalculateValue(playerhand):
    score=0
    for x in range(0,5):
        card=playerhand.GetCard(x)
        score=score+card.GetNumber()
        colour=card.GetColour()
        if colour=="red":
            score=score+5
        elif colour =="blue":
            score=score+15
        else:
            score=score+15
    return score
score1=CalculateValue(Player1)
score2=CalculateValue(Player2)
if score1>score2:
    print("player 1 wins")
elif score2>score1:
    print("Player2 wins")
else :
    print("drawww")
