import random
import sqlite3
con = sqlite3.connect("map.db")
cur = con.cursor()

def testadj(pro:str,direction:str)->bool:
    req= "SELECT [" + pro + "] FROM adjacence WHERE nom = '" + direction + "';"
    print(req)
    return cur.execute(req).fetchone()

def ttadj(region):
    req= "SELECT nom FROM adjacence WHERE " + region + " = 1 ;"
    print(req)
    return cur.execute(req).fetchall()

class Rules():
    def __init__(self , lssoldat):
        self.lssoldat = lssoldat
    
    def toursolve(self):
        #ajouter la mobilisation ...
        for soldat in lssoldat:
            if soldat.action[0] == "att":
                soldat.att(soldat.action[1], lssoldat)
            elif soldat.action[0] == "soutatt":
                soldat.soutatt(soldat.action[1], lssoldat)
            elif soldat.action[0] == "soutdef":
                soldat.soutdef(soldat.action[1], lssoldat)
            elif soldat.action[0] == "hold":
                soldat.hold(soldat.action[1])
        for soldat in lssoldat:
            if soldat.nbatt > nbdef:
                lsregionadj = ttajd(soldat.region)
                for reg in regionadj:
                    for sol in lssoladat:
                        if sol.region == region:
                           lsregionadj.remove(region)
                if len(lsregionadj) >= 1:
                    soldat.region = lsregionadj[0]
                else:
                    lssoldat.remove(soldat)
                    
        for soldat in lssoldat:
            if soldat.action[0] == "att":
                attaque = True
                for sol in lssoldat:
                    if soldat.action[1] = sol.region :
                        attaque = False
                if attaque :
                    soldat.region = soldat.action[1]
            
        # sauvegare les position dans la bd
        # change les arsenaux conqui
        #dessine la carte
        
        
        
class Soldat():
    def __init__(self , faction , region):
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
        if testadj(self.region, region):
            self.action = ("att", region)
            for sol in lssoldat:
                if sol.region == region:
                    sol.nbatt += 1
                    sol.action = ("hold" , sol.region)
    
    def soutatt(self, region, lssoldat):
        if testadj(self.region, region):
            self.action = ("soutatt", region)
            for sol in lssoldat:
                if sol.region == region:
                    sol.nbatt += 1
                    sol.action = ("hold" , sol.region)
                    
    def soutdef(self, region, lssoldat):
        if testadj(self.region, region):
            self.action = ("soutdef", region)
            for sol in lssoldat:
                if sol.region == region:
                    sol.nbdef += 1
    
    def hold(self, region):
        if self.region == region:
            self.nbdef +=1
    


        
