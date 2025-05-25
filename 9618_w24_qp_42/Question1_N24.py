class EventItem:
    #DECLARE EventName :STRING
    #DECLARE Type : STRING
    #DECLARE Difficulty : INTEGER

    def __init__(self,EventnameP,TypeP,DifficultyP):
        self.__EventName=EventnameP
        self.__Type=TypeP
        self.__Difficulty=DifficultyP

    def GetName(self):
        return self.__EventName
    def GetDifficulty(self):
        return self.__Difficulty
    def GetType(self):
        return self.__Type
    


Group=[] #EventItem
Group=[EventItem("Bridge","jump",3),
       EventItem("Water wade","swim",4),
       EventItem("Gridlock","drive",2),
       EventItem("Wall on wall","jump",4)] 


class Character():
    #DECLARE CharacterName: STRING
    #DECLARE Swim :INTEGER
    #DECLARE Run :INTEGER
    #DECLARE Drive :INTEGER

    def __init__(self,CharacterNameP,JumpP,SwimP,RunP,DriveP):
        self.__CharacterName=CharacterNameP
        self.__Jump=JumpP
        self.__Swim=SwimP
        self.__Run=RunP
        self.__Drive=DriveP
    def GetName(self):
        return self.__CharacterName
    def CalculateScore(self,eventtype,difficulty):
        skilllevel = 0
        if eventtype=="Run":
            skilllevel=self.__Run
        elif eventtype=="jump":
            skilllevel=self.__Jump
        elif eventtype=="swim":
            skilllevel=self.__Swim
        elif eventtype=="Drive":
            skilllevel=self.__Drive
        if skilllevel<difficulty:
            difference=difficulty-skilllevel
            if difference==1:
                return 80
            elif difference==2:
                return 60
            elif difference==3:
                return 40
            elif difference==4:
                return 20           
        elif skilllevel>=difficulty:
            return 100
P1 = Character("Tarz", 5, 3, 5, 1) 
P2 = Character("Geni", 2, 2, 3, 4) 

p1points=0
p2points=0
for x in range(len(Group)):
    P1EventScore=P1.CalculateScore(Group[x].GetType(),Group[x].GetDifficulty())
    p2EventScore=P2.CalculateScore(Group[x].GetType(),Group[x].GetDifficulty())

    if P1EventScore>p2EventScore:
        p1points+=1
    elif p2EventScore>P1EventScore:
        p2points+=1
    else:
        print("draw")

if p1points>p2points:
    print(P1.GetName(),"you won with",p1points)
elif p2points>p1points:
    print(P1.GetName(),"you won with",p2points)
else:
    print("issa draw")