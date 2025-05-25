#DECLARE Animals : ARRAAY[0:9] OF STRING
global Animals
Animals=[]
Animals.append("Horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaro")
Animals.append("tiger")

def SortDescending():
    ArrayLength=10
    for x in range(0,ArrayLength):
        for y in range(0,ArrayLength-x-1):
            if Animals[y][0]<Animals[y+1][0]:
                Temp=Animals[y]
                Animals[y]=Animals[y+1]
                Animals[y+1]=Temp

SortDescending()
for x in range(10):
    print(Animals[x])






