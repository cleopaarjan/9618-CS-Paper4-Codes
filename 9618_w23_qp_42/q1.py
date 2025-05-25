#DECLARE StackVowel : ARRAY[0:99] OF STRING
#DECLARE StackConsonant : ARRAY[0:99] OF STRING
global StackVowel
global StackConsonent
StackVowel=[""]*100
StackConsonent=[""]*100

global VowelTop
global ConsonentTop

VowelTop=0 #INTERGER
ConsonentTop=0 #INTERGER

def PushData(Letter):
    global StackVowel
    global StackConsonent
    global VowelTop
    global ConsonentTop
    global StackConsonent

    if Letter=="a" or Letter=="e" or Letter=="i" or Letter=="u":
        if VowelTop==100:
            print("The Vowel Stack is full")
        else:
            StackVowel[VowelTop]=Letter
            VowelTop+=1
    else:
        if ConsonentTop==100:
            print("The Consonent stack is full")
        else:

            StackConsonent[ConsonentTop] = Letter
            ConsonentTop=ConsonentTop+1

def ReadData():
    try:


        file=open("StackData.txt","r")
        for line in file:
            PushData(line.strip())
        file.close()
    except IOError:
        print("The File dosenot Exist")

def Popvowel():
    global StackVowel
    global VowelTop

    if VowelTop==0:
        return "No Data"
    else:
         VowelTop=VowelTop-1
         PoppedItem=StackVowel[VowelTop]
         return PoppedItem 
def PopConsonent():
    global StackConsonent
    global ConsonentTop

    if ConsonentTop==0:
        return "no Data"
    else:
        ConsonentTop=ConsonentTop-1
        PoppedItem=StackConsonent[ConsonentTop]
        return PoppedItem

ReadData()
combine=""
for x in range(5):
    UserChoice=input("Enter the vowel or consonent: ")
    if UserChoice.lower()=="vowel":
        PoppedVowel=Popvowel()
        if PoppedVowel=="No Data":
            print("no vowels available" )
        else:
            combine=combine+PoppedVowel
    elif UserChoice.lower()=="consonent":
        PoppedConsonent=PopConsonent()
        if PoppedConsonent=="NoData":
            print("No Consonent Availabe")
        else:
            combine=combine+PoppedConsonent
print(combine)

