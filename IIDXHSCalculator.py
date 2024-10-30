##VERSION 3.0
import bisect

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
    
wnlist=[50,53,56,59,62,65,68,71,75,78,81,84,87,90,93,96,\
        100,103,106,109,112,115,118,121,125,128,131,134,137,140,143,146,\
        150,153,156,159,162,165,168,171,175,178,181,184,187,190,193,196,\
        200,203,206,209,212,215,218,221,225,228,231,234,237,240,243,246,\
        250,253,256,259,262,265,268,271,275,278,281,284,287,290,293,296,\
        300,303,306,309,312,315,318,321,325,328,331,334,337,340,343,346,\
        350,353,356,359,362,365,368,371,375,378,381,384,387,390,393,396,\
        400,403,406,409,412,415,418,421,425,428,431,434,437,440,443,446,\
        450,453,456,459,462,465,468,471,475,478,481,484,487,490,493,496,\
        500,503,506,509,512,515,518,521,525,528,531,534,537,540,543,546,\
        550,553,556,559,562,565,568,571,575,578,581,584,587,590,593,596,\
        600,603,606,609,612,615,618,621,625,628,631,634,637,640,643,646,\
        650,653,656,659,662,665,668,671,675,678,681,684,687,690,693,696,\
        700,703,706,709,712,715,718,721,725,728,731,734,737,740,743,746,\
        750,753,756,759,762,765,768,771,775,778,781,784,787,790,793,796,\
        800,803,806,809,812,815,818,821,825,828,831,834,837,840,843,846,\
        850,853,856,859,862,865,868,871,875,878,881,884,887,890,893,896,\
        900,903,906,909,912,915,918,921,925,928,931,934,937,940,943,946,\
        950,953,956,959,962,965,968,971,975,978,981,984,987,990,993,996,999]

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
    i=bisect.bisect_right(wnlist,whiteNumber)
    return wnlist[i-1]

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
            output.append(f"{hispeed[0]:<5} {multiplier:<7} WN = {roundWhiteNumber(whiteNumber)}")
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
            print(f"{i+1}. {styles[i].name}")
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
    