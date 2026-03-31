from PIL import Image
import sqlite3

con = sqlite3.connect("/home/tutu/Bureau/jeux test image/mapi.db")
cur = con.cursor()
"""
# Open the base image
base_img = Image.open("diplo.jpg")

# Duplicate it
result_img = base_img.copy()

# Open the image you want to place on top
overlay_img = Image.open("Greyjoy.png")

# Optional: resize overlay
overlay_img = overlay_img.resize((100, 130))


overlay_img = overlay_img.convert("RGBA")

# Optional: position (x, y)
#position = (1900, 130)
#position = (2300, 600)
#position = (2900, 1000)

##position = (1800, 1400)

#position = (2550, 1400)
#position = (1200, 1700)

##position = (1600, 2000)

#position = (2000, 2100)

##position = (2600, 2050)

#position = (1600, 2400)

##position = (1800, 2800)



##position = (1200, 3050)
##position = (900, 3100)
##position = (1050, 3250)

##position = (1200, 3900)
##position = (2500, 4050)
##position = (2450, 3600)
##position = (1700, 4900)

##position = (900, 4800)
##position = (1000, 5200)
##position = (800, 5750)

##position = (2300, 5650)
##position = (3100, 5550)
##position = (3600, 5000)
##position = (2000, 5200)

##position = (2900, 4900)
##position = (2800, 4600)
##position = (3250, 4600)

##position = (3100, 3800)
##position = (3900, 4000)
##position = (4000, 3000)
position = (4100, 4350)

# If overlay has transparency (PNG)
result_img.paste(overlay_img, position, overlay_img)
result_img = result_img.convert("RGBA")

# Save the final image
result_img.save("final_image.png")
"""
def apparition(arsenal:str, region: str) -> str:
    req = "UPDATE position SET arsenal = ? WHERE nom = ? ;"
    #cur.execute("UPDATE position SET arsenal= ["+ arsenal +"] WHERE nom=["+ region +"];")
    cur.execute(req,(arsenal, region))
    con.commit()
    
def coor(region: str):
    cor = "SELECT coor_arsenal FROM position WHERE nom = ?;"
    res = cur.execute(cor,(region,)).fetchone()
    clean = res[0].strip("()")
    return tuple(int(v.strip()) for v in clean.split(","))

def duplicate(carte: str):
    base = Image.open(carte)
    dup = base.copy()
    dup.save("copy.png")
    
def affichage(region, famille, carte: str):
    # Open the base image
    result_img = Image.open(carte)
    nom = famille +".png"
    
    overlay_img = Image.open(nom)
    overlay_img = overlay_img.resize((100, 130))

        
    overlay_img = overlay_img.convert("RGBA")
    position = coor(region)
    
    result_img.paste(overlay_img, position, overlay_img)
    
    result_img = result_img.convert("RGBA")
    
    result_img.save(carte)        
        
        
        

def creation_carte(carte: str):
    list = cur.execute("SELECT nom, arsenal FROM position WHERE arsenal IS NOT NULL").fetchall()
    for x, y in list:
       affichage(x, y, carte)
