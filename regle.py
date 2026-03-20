import random
import sqlite3
import time
con = sqlite3.connect("mapi.db")
cur = con.cursor()

def testadj(pro:str,direction:str)->bool:
    #req= "SELECT [" + pro + "] FROM adjacence WHERE nom = '" + direction + "';"
    req= "SELECT [" + pro + "] FROM test WHERE nom = '" + direction + "';"
    print(req)
    return cur.execute(req).fetchone()

def ttadj(region):
    #req= "SELECT nom FROM adjacence WHERE " + region + " = 1 ;"
    req= "SELECT nom FROM test WHERE " + region + " = 1 ;"
    print(req)
    return cur.execute(req).fetchall()

class Rules():
    def __init__(self , lssoldat):
        self.lssoldat = lssoldat
    
    def toursolve(self):
        #ajouter la mobilisation ...
        for soldat in lssoldat:
            if soldat.action[0] == "att":
                for sol in lssoldat:
                    if sol.region == soldat.action[1]:
                        for s in lssoldat :
                            if s.region == sol.action[1]:
                                s.nbatt = s.nbatt - 1
                        sol.hold()
        for sol in lssoldat:
            print(sol.faction , "|" ,sol.region , "|" ,sol.action, "|" ,sol.nbatt , sol.nbdef)
        print("################################")

                
        for soldat in lssoldat:
            if soldat.nbatt > soldat.nbdef:
                lsregionadj = ttadj(soldat.region)
                for reg in lsregionadj:
                    for sol in lssoldat:
                        if sol.region == reg:
                           lsregionadj.remove(region)
                if len(lsregionadj) >= 1:
                    soldat.region = lsregionadj[0][0]
                else:
                    lssoldat.remove(soldat)
                    
        for soldat in lssoldat:
            if soldat.action[0] == "att":
                attaque = True
                for sol in lssoldat:
                    if soldat.action[1] == sol.region :
                        attaque = False
                if attaque :
                    soldat.region = soldat.action[1]
        for soldat in lssoldat:
            soldat.hold()
            soldat.nbdef = 0
            soldat.nbatt = 0
            
        # sauvegare les position dans la bd
        # change les arsenaux conqui
        #dessine la carte
        
        
        
class Soldat():
    def __init__(self , faction , region):
        reglibre = True
        for sol in lssoldat:
            if sol.region == region:
                reglibre = False
                
        if reglibre : 
            self.faction = faction
            self.region = region
            self.nbatt = 0
            self.nbdef = 0
            self.action = ("hold", region)
            
    def att(self,region, lssoldat):
        print(testadj(self.region, region))
        if testadj(self.region, region):
            self.action = ("att", region)
            for sol in lssoldat:
                if sol.region == region:
                    sol.nbatt += 1
                    sol.action = ("hold" , sol.region)
    
    def soutatt(self, region, lssoldat):
        print(testadj(self.region, region))
        if testadj(self.region, region):
            self.action = ("soutatt", region)
            for sol in lssoldat:
                if sol.region == region:
                    sol.nbatt += 1
                    sol.action = ("hold" , sol.region)
                    
    def soutdef(self, region, lssoldat):
        print(testadj(self.region, region))
        if testadj(self.region, region):
            self.action = ("soutdef", region)
            for sol in lssoldat:
                if sol.region == region:
                    sol.nbdef += 1
    
    def hold(self):
        self.action = ("hold", self.region)
        self.nbdef +=1
    

while True : 
    lssoldat = []
    s1 = Soldat("stark","Field1")
    lssoldat.append(s1)
    s2 = Soldat("stark","Field2")
    lssoldat.append(s2)
    s5 = Soldat("lannister","Field5")
    lssoldat.append(s5)



    s1.att("Field5",lssoldat)
    #s2.soutatt("Field5",lssoldat)
    s2.hold()
    s5.att("Field2",lssoldat)
    game = Rules(lssoldat)

    for sol in lssoldat:
        print(sol.faction , "|" ,sol.region , "|" ,sol.action, "|" ,sol.nbatt , sol.nbdef)
    print("################################")


    game.toursolve()


    for sol in lssoldat:
        print(sol.faction , "|" ,sol.region , "|" ,sol.action, "|" ,sol.nbatt , sol.nbdef)
    print("################################")
    
    time.sleep(30)

        
