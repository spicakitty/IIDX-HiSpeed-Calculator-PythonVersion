## VERSION 1.0
## gn=170000/(bpm*hs*(1000/(1000-wn-lift)))
s=9
screenlimits=[75,75,75,75,70,70,50,47,59,50,50,70]
l=7
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



def findwn(bpm,hs,gn):
    return 1000-((bpm*hs*gn)/174)

def findbpm(gn,hs):
    return 174000/(gn*hs*(1000/(1000-screenlimits[s])))

def hscalc(s):
    print("-"*30)
    gn=int(input("Green Number: "))
    bpm=float(input("BPM: "))
    for hs in hispeed[s]:
        wn=findwn(bpm,hs[1],gn)
        if wn>=screenlimits[s]:
            m=f"(x{hs[1]})"
            print(f"{hs[0]:<5} {m:<7} WN = {round(wn,2)}")
    return

def towelcalc(s):
    print("-"*30)
    gn=int(input("Green Number: "))
    bpm=float(input("BPM: "))
    for hs in hispeed[s]:
        wn=findwn(bpm,hs[1],gn)
        if wn>=screenlimits[s]:
            m=f"(x{hs[1]})"
            print(f"{hs[0]:<5} {m:<7} Towel = {round(((wn-screenlimits[s])/(1000-screenlimits[s]))*1000,2)}")
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
