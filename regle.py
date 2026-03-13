import random
import sqlite3
con = sqlite3.connect("mapi.db")
cur = con.cursor()

def testadj(pro:str,direction:str)->bool:
    req= "SELECT [" + pro + "] FROM adjacence WHERE nom = '" + direction + "';"
    print(req)
    return cur.execute(req).fetchone()



class Rules():
    def __init__(self , lssoldat):
        self.lssoldat = lssoldat
    
    def toursolve(self):
        #ajouter la mobilisation ...
        for soldat in lssoldat:
            if soldat.action[0] = "att":
                soldat.att(soldat.action[1], lssoldat)
            elif soldat.action[0] = "soutatt":
                soldat.soutatt(soldat.action[1], lssoldat)
            elif soldat.action[0] = "soutdef":
                soldat.soutdef(soldat.action[1], lssoldat)
            elif soldat.action[0] = "hold":
                soldat.hold(soldat.action[1])
        ##voirlesdeplacenment
        # parcour la liste et bouge les armee vaincu
        # deplace les armee victorieurse
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
                if sol.region = region:
                    sol.nbatt += 1
                    sol.action = ("hold" , sol.region)
    
    def soutatt(self, region, lssoldat):
        if testadj(self.region, region):
            self.action = ("soutatt", region)
            for sol in lssoldat:
                if sol.region = region:
                    sol.nbatt += 1
                    sol.action = ("hold" , sol.region)
                    
    def soutdef(self, region, lssoldat):
        if testadj(self.region, region):
            self.action = ("soutdef", region)
            for sol in lssoldat:
                if sol.region = region:
                    sol.nbdef += 1
    
    def hold(self, region):
        if self.region == region:
            self.nbdef +=1
    
        
        
        

        
