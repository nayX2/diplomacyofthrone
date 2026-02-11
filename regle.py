import random
import sqlite3
con = sqlite3.connect("map.db")
cur = con.cursor()

def testadj(pro:str,direction:str)->bool:
    req= "SELECT [" + pro + "] FROM adjacence WHERE nom = '" + direction + "';"
    print(req)
    return cur.execute(req).fetchone()

    
class Region():
    def __init__(self, nom, arsenal, faction, mer, soldat):
        self.nom = nom
        self.arsenal = arsenal
        self.faction = faction
        self.mer = mer
        self.soldat = soldat

        

class Soldat():
    def __init__(self , region: Region , faction, lssoldat , action):
        for sol in lssoldat:
            if sol.region == region:
                reglibre = False
                
        if reglibre :    
            self.faction = faction
            self.region = region
            self.action = []
            lssoldat.append((faction, region ))
    
    def move(self, region):
        if testadj(self.region, region.nom):
            if region.soldat == None:
                #region.addsoldat(self)
                #self.region.removesoldat
                #
                #self.region = region.nom
                self.action.append(("push",region.soldat))
                
                
            elif region.soldat.faction == self.faction :
                return None
            
            else :
                region.soldat.action.append(("attaqué",self))
                self.action.append(("push",region.soldat))
                
    def defend(self):
        if testadj(self.region, region.nom):
            if region.soldat.faction == self.faction :
                self.action.append(("defend",self.region))

    def soutient(self, region):
        if testadj(self.region, region.nom):
            if region.soldat.faction == self.faction :
                
                region.soldat.action.append(("defendu",self))
                self.action.append(("soutient",region))

    


def attaquecollision(lssoldat):
    for soldat in lssoldat:
        sousattaque = False
        for action , _ in soldat.action:
            if action == "attaqué":
                sousattaque = True
        if sousattaque:
            for action , region in soldat.action:
                if action == "push" :
                    region.soldat.action.remove(( "attaqué" , soldat.region))
                elif action == "defend":
                    region.soldat.action.remove(( "defendu" , soldat.region))
            
            soldat.action = [("defend",soldat)]
    return lssoldat

def attaqueaction(lssoldat):
    pass

    
def resolution(lssoldat):
    random.shuffle(lssoldat)
    
    attaquecollision(lssoldat)
    
    attaqueaction(lssoldat)
    
    
    







