#DECLARE Jobs:ARRAY[0:99] OF INTEGER
#DECLARE NumberOfJobs : INTEGER

global Jobs
global NumberOfJobs
Jobs=[]

def Initialise():
    global Jobs
    global NumberOfJobs
    for x in range(100):
        Jobs.append([-1,-1])
    NumberOfJobs=0

def Addjobs(JobNumber,Priority):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs<100:
        Jobs[NumberOfJobs][0]=JobNumber
        Jobs[NumberOfJobs][1]=Priority
        #Jobs[NumberOfJobs]=[JobNumber][Prirotity]

        print("ADDED")
        NumberOfJobs+=1
    else:
        print("NOT ADDED")


Initialise()

Addjobs(12,10)
Addjobs(526,9)
Addjobs(526,9)
Addjobs(33,8)
Addjobs(78,1)

def InsersionSort():
    global Jobs
    global NumberOfJobs

    for pointer in range(1,NumberOfJobs):
        #WE USUALLY STORE valuetoINSERT as your temp variables
        valuejob=Jobs[pointer][0]
        valuepriotity=Jobs[pointer][1]

        holeposition=pointer
        while holeposition>0 and Jobs[holeposition-1][1]>valuepriotity:
            Jobs[holeposition][0]=Jobs[holeposition-1][0]
            Jobs[holeposition][1]=Jobs[holeposition-1][1]
            holeposition-=1
        Jobs[holeposition][0]=valuejob
        Jobs[holeposition][1]=valuepriotity

InsersionSort()
print(Jobs)


def PrintArray():

    global Jobs
    global NumberOfJobs

    for x in range(NumberOfJobs):
        global Jobs
        global NumberOfJobs
        for x in range(NumberOfJobs):
            Job=Jobs[x][0]
            print=Jobs[x][1]
           # line=str(Job)+"Priority: "+str(Priority)
            #print(line)

InsersionSort()
PrintArray()