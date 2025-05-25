class Character():
    #PRIVATE Name:STRING
    #PRIVATE XCoordinate:INTEGER
    #PRIVATE YCoordinate:INTEGER

    def __init__(self,NameP,XCoordinateP,YCoordinateP):
        self.__Name=NameP
        self.__XCoordinator=XCoordinateP
        self.__YCoordinator=YCoordinateP

    def getName(self):
        return self.__Name
    def getX(self):
        return self.__XCoordinator
    def getY(self):
        return self.__YCoordinator  #5marks ettuk porjontoh
    def ChangePosition(self,Xchange,YChange):
        self.__XCoordinator=self.__XCoordinator+Xchange
        self.__YCoordinator=self.__YCoordinator+YChange
#DECLARE Characters : ARRAY [0:9] OF Character
characters=[]
try:
    file=open("Characters.txt","r")
    for x in range(10):
        name=file.readline().strip()
        xcord=int(file.readline().strip())
        ycord=int(file.readline().strip())
        CharactersObject=Character(name,xcord,ycord)
        characters.append(CharactersObject)
except:
    print("File not found")
print(characters)    
Flag = True
while Flag:
    username=input("Enter a name: ")
    for x in range(10):
        nameformobject=characters[x].getName()
        if username.lower()==nameformobject.lower():
            Position=x
            Flag=False
print(Position)
NewFlag=True
while NewFlag:
    direction=input("Enter W/A/S/D: ")
    if direction.upper()=="A":
        characters[Position].ChangePosition(-1,0)
        NewFlag=False
    elif direction.upper()=="W":
        characters[Position].ChangePosition(0,1)
        NewFlag=False 

    elif direction.upper()=="S":
        characters[Position].ChangePosition(0,-1)
        NewFlag=False
    elif direction.upper()=="D":
        characters[Position].ChangePosition(1,0)
        newFlag=False


print(username,"Has changed coordinates to x=",characters[Position].getX(),"and y=",characters[Position].getY())
