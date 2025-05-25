class Horse():
    def __init__(self,NameP,MaxFenceHeightP,PrecentageSuccessP):
        self.__Name=NameP #STRING
        self.__MaxFenceHeight=MaxFenceHeightP #INTEGER
        self.__PercentageSucess=PrecentageSuccessP #INETEGR

    def GetName(self):
        return self.__Name
    def GetMaxFenceHight(self):
        return self.__MaxFenceHeight
    def Sucess(self,fenceheightP,riskP):
        if fenceheightP>self.__MaxFenceHeight:
            return 20
        else:
            if riskP==5:
                sucessful=self.__PercentageSucess*0.6
                return sucessful
            elif riskP==4:
                sucessful=self.__PercentageSucess*0.7
                return sucessful
            elif riskP==3:
                sucessful=self.__PercentageSucess*0.8
                return sucessful
            elif riskP==2:
                sucessful=self.__PercentageSucess*0.9
                return sucessful
            elif riskP==1:
                sucessful=self.__PercentageSucess*1.0
                return sucessful




Horses=[[] for x in range(2)] #array:Horse
Horses[0]=Horse("Beauty",150,72)
Horses[1]=Horse("Jet",160,65)

print(Horses[0].GetName(),Horses[1].GetName())


class Fence:
    def __init__(self,HeightP,RiskP):
        self.__Height=HeightP #INTEGER
        self.__Risk=RiskP #INTEGER
    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk
    


Courses=[]
for x in range(4):

    fenceheight=int(input("height: "))
    while fenceheight <=70 or fenceheight>=180:
        fenceheight=int(input("height: "))
    risk=int(input("risk: "))
    while risk <1 or risk>5:
        risk=int(input("risk: "))
    
    Courses.append(Fence(fenceheight,risk))

for x in range(len(Courses)):
    for y in range(len(Horses)):
        height=Courses[x].GetHeight()
        rissk=Courses[x].GetRisk()
        success=Horses[y].Sucess(height,rissk)
        horsiename=Horses[y].GetName()
        print("The Horse",str(horsiename),"at fence",x+1,round(success),"%chance of success")

horseavg=[]
for x in range(len(Horses)):
    totalsucess=0
    for y in range(len(Courses)):
        
        height=Courses[x].GetHeight()
        rissk=Courses[x].GetRisk()
        success=Horses[y].Sucess(height,rissk)
        horsiename=Horses[y].GetName()
        totalsucess=totalsucess+success
        avg_success=totalsucess/4
        horseavg.append(avg_success,horsiename)

if horseavg[0][0]>horseavg[1][0]:
    print(horseavg[0][1],"has more avg")
    
elif horseavg[1][1]>horseavg[0][1]:
    print(horseavg[1][1],"has more avg")
