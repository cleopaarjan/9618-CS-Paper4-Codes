class TreasureChest():
    #PRIVATE question :STRING
    #PRIVATE answer :INTEGER
    #PRIVATE points : INTEGER

    def __init__(self,questionP,pointsp,answerP):
        self.__question=questionP
        self.__points=pointsp
        self.__answer=answerP

    def getQuestion(self):
        return self.__question
    
    def checkAnswer(seld,answerpp):
        if int(self.__answer)==answerpp:
            return True
        else:
            return False
    
    def getPoints(self, attempts): 
            if attempts == 1: 
                return int(self.__points) 
            elif attempts == 2: 
                return int(self.__points) // 2 
            elif attempts == 3 or attempts == 4: 
                return int(self.__points) // 4 
            else: 
                return 0 
            

    

    
#DECLARE arrayTreasure as TreasureChest 

arrayTreasure=[]
def readData():
    filename="TreasureChestData.txt"
    try:
        file=open(filename,"r")
        datafeched=(file.readline()).strip()
        while datafeched != " ":
            question=datafeched
            answer=(file.readline()).strip()
            points=(file.readline()).strip()

            arrayTreasure.append(TreasureChest(question,answer,points))
            datafeched=(file.readline()).strip()

        file.close()
    except IOError:
        print("File not found")

readData() 
choice = int(input("Pick a treasure chest to open")) 
if choice > 0 and choice < 6: 
        
    result = False 
    attempts = 0 
    while result == False: 
      answer = int(input(arrayTreasure[choice-1].getQuestion())) 
      result = arrayTreasure[choice-1].checkAnswer(answer) 
      attempts = attempts + 1 
      print(int(arrayTreasure[choice-1].getPoints(attempts)))


    #C2345 balsal