## VERSION 1.1
import bisect
## gn=170000/(bpm*hs*(1000/(1000-wn-lift)))
displayoverlimit=True
s=9
screenlimits=[75,75,75,75,70,70,50,46,59,46,46,70]
l=7
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
# HAPPY SKY = 59
styles=["3rd","4th","5th","6th","7th","8th-9th","10th","IIDX RED","HAPPY SKY","DistorteD","GOLD-EMPRESS","Fast Songs"]

hispeed=[[("LS2",round(1/3,2)),("LS1",1/2),("HS0",1),("HS1",2),("HS2",3),("HS3",4)],\
    [("LS2",round(1/3,2)),("LS1",1/2),("HS0",1),("HS1",2),("HS2",2.75),("HS3",3.5)],\
    [("LS2",round(1/3,2)),("LS1",1/2),("HS0",1),("HS1",2),("HS2",2.5),("HS3",3)],\
    [("LS1",1/2),("HS0",1),("HS1",2),("HS2",2.5),("HS3",3),("HS4",3.5)],\
    [("HS0",1),("HS1",2),("HS2",2.5),("HS3",3),("HS4",3.5)],\
    [("HS0",1),("HS1",2),("HS2",2.5),("HS3",3),("HS4",3.5)],\
    [("HS0",1),("HS0.5",1.5),("HS1",2),("HS1.5",2.25),("HS2",2.5),("HS2.5",2.75),("HS3",3),("HS3.5",3.25),("HS4",3.5)],\
    [("HS0",1),("HS0.5",1.5),("HS1",2),("HS1.5",2.25),("HS2",2.5),("HS2.5",2.75),("HS3",3),("HS3.5",3.25),("HS4",3.5),("HS4.5",3.75),("HS5",4)],\
    [("HS0",1),("HS0.5",1.5),("HS1",2),("HS1.5",2.25),("HS2",2.5),("HS2.5",2.75),("HS3",3),("HS3.5",3.25),("HS4",3.5),("HS4.5",3.75),("HS5",4)],\
    [("HS0",1),("HS0.5",1.5),("HS1",2),("HS1.5",2.25),("HS2",2.5),("HS2.5",2.75),("HS3",3),("HS3.5",3.25),("HS4",3.5),("HS4.5",3.75),("HS5",4)],\
    [("HS0",1),("HS0.5",1.5),("HS1",2),("HS1.5",2.25),("HS2",2.5),("HS2.5",2.75),("HS3",3),("HS3.5",3.25),("HS4",3.5),("HS4.5",3.75),("HS5",4)],\
    [("HS0",1),("HS1",1.5),("HS2",2),("HS3",2.5),("HS4",3)]]

def roundwn(wn):
    i=bisect.bisect_right(wnlist,wn)
    return wnlist[i-1]

def findwn(bpm,hs,gn):
    return 1000-((bpm*hs*gn)/174)

def findtowel(wn):
    return ((wn-screenlimits[s])/(1000-screenlimits[s]))*1000

def findbpm(gn,hs):
    return 174000/(gn*hs*(1000/(1000-screenlimits[s])))

def findgn(bpm,hs,wn):
    return 170000/(bpm*hs*(1000/(1000-wn)))

def hscalc(s):
    output=[]
    hilighted=False
    print("-"*30)
    gn=int(input("Green Number: "))
    bpm=float(input("BPM: "))
    for hs in hispeed[s]:
        wn=findwn(bpm,hs[1],gn)
        if wn>=max([screenlimits[s],50]):
            m=f"(x{hs[1]})"
            output.append(f"{hs[0]:<5} {m:<7} WN = {roundwn(wn)}")
        else:
            if not hilighted: 
                output[-1]+='\t\t**********'
                hilighted=True
            if displayoverlimit:
                m=f"(x{hs[1]})"
                output.append(f"{hs[0]:<5} {m:<7} GN = {round(findgn(bpm,hs[1],screenlimits[s]),2)}")
    for line in output: print(line)
    return

def towelcalc(s):
    output=[]
    hilighted=False
    print("-"*30)
    gn=int(input("Green Number: "))
    bpm=float(input("BPM: "))
    for hs in hispeed[s]:
        wn=findwn(bpm,hs[1],gn)
        if wn>=screenlimits[s]:
            m=f"(x{hs[1]})"
            output.append(f"{hs[0]:<5} {m:<7} Towel = {round(findtowel(wn),2)}")
        else:
            if not hilighted: 
                output[-1]+='\t\t**********'
                hilighted=True
            if displayoverlimit:
                m=f"(x{hs[1]})"
                output.append(f"{hs[0]:<5} {m:<7} GN = {round(findgn(bpm,hs[1],screenlimits[s]),2)}")
    for line in output: print(line)
    return

def maxbpmcalc(s):
    print("-"*30)
    gn=int(input("Green Number: "))
    for hs in hispeed[s]:
        m=f"(x{hs[1]})"
        print(f"{hs[0]:<5} {m:<7} --> {round(findbpm(gn,hs[1]),2)}")
    return

def stylechoose():
    while True:
        print("-"*30)
        print("1. 3rd Style")
        print("2. 4th Style")
        print("3. 5th Style")
        print("4. 6th Style")
        print("5. 7th Style")
        print("6. 8th Style - 9th Style")
        print("7. 10th Style")
        print("8. IIDX RED")
        print("9. HAPPY SKY")
        print("10. DistorteD")
        print("11. GOLD-EMPRESS")
        print("12. Fast Songs")
        i=input()
        v=True
        for c in i:
            if c not in "1234567890":
                print("Incorrect input")
                v=False
                break
        if v:
            if int(i)>0 and int(i)<13:
                return int(i)-1
            else: print("Incorrect input")
        
        # if len(i)==1 and i in "12345678":
        #     return int(i)-1
        # else:
        #     print("Incorrect input.")


while True:
    print("-"*30)
    print(f"Current style: {styles[s]}")
    print("1. Calculate Hi-Speed")
    print("2. Calculate Towel")
    print("3. Calculate Max BPM")
    print("4. Change style")
    print("5. Exit")
    n=input()
    if n=="1": hscalc(s)
    elif n=="2": towelcalc(s)
    elif n=="3": maxbpmcalc(s)
    elif n=="4": s=stylechoose()
    elif n=="5": break
    else: print("Incorrect input.")
