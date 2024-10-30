##VERSION 3.1
import math

playstyle=[["Single","Double"],[298,335]]
ps=0
displayoverlimit=True
s=8
ignoreScreenLimit=False

class Style:
    def __init__(self, name, screenlimit, hispeedvalues):
        self.name=name
        self.screenlimit=screenlimit
        self.hispeedvalues=hispeedvalues

    def getScreenLimit(self):
        if ignoreScreenLimit:
            return 50
        else:
            return self.screenlimit
styles=[
Style("3rd Style",75,[("LS2",round(1/3,2)),("LS1",1/2),("HS0",1),("HS1",2),("HS2",3),("HS3",4)]),
Style("4th Style",75,[("LS2",round(1/3,2)),("LS1",1/2),("HS0",1),("HS1",2),("HS2",2.75),("HS3",3.5)]),
Style("5th Style",75,[("LS2",round(1/3,2)),("LS1",1/2),("HS0",1),("HS1",2),("HS2",2.5),("HS3",3)]),
Style("6th Style",75,[("LS1",1/2),("HS0",1),("HS1",2),("HS2",2.5),("HS3",3),("HS4",3.5)]),
Style("7th Style",70,[("HS0",1),("HS1",2),("HS2",2.5),("HS3",3),("HS4",3.5)]),
Style("8th Style",70,[("HS0",1),("HS1",2),("HS2",2.5),("HS3",3),("HS4",3.5)]),
Style("9th Style",46,[("HS0",1),("HS1",2),("HS2",2.5),("HS3",3),("HS4",3.5)]),
Style("10th Style",46,[("HS0",1),("HS0.5",1.5),("HS1",2),("HS1.5",2.25),("HS2",2.5),("HS2.5",2.75),("HS3",3),("HS3.5",3.25),("HS4",3.5)]),
Style("IIDX RED",46,[("HS0",1),("HS0.5",1.5),("HS1",2),("HS1.5",2.25),("HS2",2.5),("HS2.5",2.75),("HS3",3),("HS3.5",3.25),("HS4",3.5),("HS4.5",3.75),("HS5",4)]),
Style("HAPPY SKY",59,[("HS0",1),("HS0.5",1.5),("HS1",2),("HS1.5",2.25),("HS2",2.5),("HS2.5",2.75),("HS3",3),("HS3.5",3.25),("HS4",3.5),("HS4.5",3.75),("HS5",4)]),
Style("DistorteD",46,[("HS0",1),("HS0.5",1.5),("HS1",2),("HS1.5",2.25),("HS2",2.5),("HS2.5",2.75),("HS3",3),("HS3.5",3.25),("HS4",3.5),("HS4.5",3.75),("HS5",4)]),
Style("GOLD-EMPRESS",46,[("HS0",1),("HS0.5",1.5),("HS1",2),("HS1.5",2.25),("HS2",2.5),("HS2.5",2.75),("HS3",3),("HS3.5",3.25),("HS4",3.5),("HS4.5",3.75),("HS5",4)]),
Style("Sakura",70,[("HS0",1),("HS1",1.5),("HS2",2),("HS3",2.5),("HS4",3)]),
Style("PSM",46,[("HS0",1),("HS1",1.5),("HS2",2),("HS3",2.5),("HS4",3)])
]

def intinput(s=""):
    while True:
        i=input(s)
        if i.isnumeric(): return int(i)
        else: print("Invalid input.")

def floatinput(s=""):
    while True:
        f=True
        i=input(s)
        for c in i:
            if not (c.isnumeric() or c=='.'):
                f=False
                break
        if f:
            return float(i)
        print("Invalid input.")

def roundWhiteNumber(whiteNumber):
    wn=50
    while(True):
        if wn+(25/8)>=whiteNumber:
            return wn
        else: wn+=25/8
    # i=bisect.bisect_right(wnlist,whiteNumber)
    # return wnlist[i-1]

def displayWhiteNumber(whiteNumber):
    if roundWhiteNumber(whiteNumber)==1000:
        return 999
    return math.floor(roundWhiteNumber(whiteNumber))

def findWhiteNumber(bpm,hispeed,greenNumber):
    return 1000-((bpm*hispeed*greenNumber)/174)

def findGreenNumber(bpm,hispeed,whiteNumber):
    return 174000/(bpm*hispeed*(1000/(1000-whiteNumber)))

def findTowel(whiteNumber):
    return ((whiteNumber-styles[s].getScreenLimit())/(1000-styles[s].getScreenLimit()))*1000

def findBPM(greenNumber,hispeed):
    return 174000/(greenNumber*hispeed*(1000/(1000-styles[s].getScreenLimit())))

def calculateHiSpeed():
    output=[]
    hilighted=False
    print("-"*30)
    bpm=floatinput("BPM: ")
    for hispeed in styles[s].hispeedvalues:
        whiteNumber=findWhiteNumber(bpm,hispeed[1],playstyle[1][ps])
        if whiteNumber>=max(styles[s].getScreenLimit(),50):
            multiplier=f"(x{hispeed[1]})"
            output.append(f"{hispeed[0]:<5} {multiplier:<7} WN = {displayWhiteNumber(whiteNumber)}")
        else:
            if not hilighted:
                if len(output)!=0:
                    output[-1]+='\t\t**********'
                hilighted=True
            if displayoverlimit:
                multiplier=f"(x{hispeed[1]})"
                
                output.append(f"{hispeed[0]:<5} {multiplier:<7} GN = {round(findGreenNumber(bpm,hispeed[1],styles[s].getScreenLimit()),2)}")
    for line in output: print(line)
    return

def calculateTowel():
    output=[]
    hilighted=False
    print("-"*30)
    bpm=floatinput("BPM: ")
    for hispeed in styles[s].hispeedvalues:
        whiteNumber=findWhiteNumber(bpm,hispeed[1],playstyle[1][ps])
        if whiteNumber>=styles[s].getScreenLimit():
            multiplier=f"(x{hispeed[1]})"
            output.append(f"{hispeed[0]:<5} {multiplier:<7} Towel = {round(findTowel(whiteNumber),2)}")
        else:
            if not hilighted:
                if len(output)!=0:
                    output[-1]+='\t\t**********'
                hilighted=True
            if displayoverlimit:
                multiplier=f"(x{hispeed[1]})"
                output.append(f"{hispeed[0]:<5} {multiplier:<7} GN = {round(findGreenNumber(bpm,hispeed[1],styles[s].getScreenLimit()),2)}")
    for line in output: print(line)
    return

def calculateMaxBPM():
    print("-"*30)
    for hispeed in styles[s].hispeedvalues:
        multiplier=f"(x{hispeed[1]})"
        print(f"{hispeed[0]:<5} {multiplier:<7} --> {round(findBPM(playstyle[1][ps],hispeed[1]),2)}")
    return

def styleChoose():
    while True:
        print("-"*30)
        for i in range(len(styles)):
            print(f"{str(i+1)+'.':>3} {styles[i].name}")
        n=intinput()
        if n>0 and n<=len(styles):
            return n-1
        else: print("Incorrect input")

def settings():
    global displayoverlimit, ignoreScreenLimit
    while True:
        print("-"*30)
        print(f"1. Change Singles GN ({playstyle[1][0]})")
        print(f"2. Change Doubles GN ({playstyle[1][1]})")
        print(f"3. Toggle displayoverlimit ({displayoverlimit})")
        print(f"4. Toggle ignoreScreenLimit ({ignoreScreenLimit})")
        print("0. Return")
        n=input()
        if n=="1": playstyle[1][0]=intinput("Singles GN: ")
        elif n=="2": playstyle[1][1]=intinput("Doubles GN: ")
        elif n=="3":
            if displayoverlimit: displayoverlimit=False
            else: displayoverlimit=True
        elif n=="4":
            if ignoreScreenLimit: ignoreScreenLimit=False
            else: ignoreScreenLimit=True
        elif n=="0": return
        else: print("Incorrect input.")

if __name__ == "__main__":
    while True:
        print("-"*30)
        print(f"Current style: {styles[s].name}")
        print(f"Current playstyle: {playstyle[0][ps]} ({playstyle[1][ps]})")
        print("1. Calculate Hi-Speed")
        print("2. Calculate Towel")
        print("3. Calculate Max BPM")
        print("4. Toggle playstyle")
        print("5. Change style")
        print("6. Settings")
        print("0. Exit")
        n=input()
        if n=="1": calculateHiSpeed()
        elif n=="2": calculateTowel()
        elif n=="3": calculateMaxBPM()
        elif n=="4":
            if ps: ps=0
            else: ps=1
        elif n=="5": s=styleChoose()
        elif n=="6": settings()
        elif n=="0": break
        else: print("Incorrect input.")
    