#Bergþór Ingi Birgirsson
#+ hjálpaði mér Frændi minn í
from random import *
with open("spil2.txt","r") as spil:
    spilastokkur=spil.read().split("\n")
spil.close()
spilari=[]
tolva=[]
for x in spilastokkur:
    randomtala=randint(0,len(spilastokkur)-1)
    spilari.append(spilastokkur[randomtala])
    spilastokkur.remove(spilastokkur[randomtala])
    if len(spilari)==26:
        break
tolva=spilastokkur
strid=[]
teljari=0
while len(spilari)!=0 and len(tolva)!=0:
    spil=str(spilari[0])
    spil=spil.split(",")
    spil2=str(tolva[0])
    spil2=spil2.split(",")
    if teljari%2==0:
        print("Þú drókst spilið",spil[0],"1. Þyngd",spil[1],"2. Mjólkurlagni dætra",spil[2],"3. Einkunn ullar",spil[3],"4. Fjöldi afkvæma",spil[4],"5. Einkunn læris",spil[5],"6. Frjósemi",spil[6],"7. Gerð/þykkt bakvöðva",spil[7],"8. Einkunn fyrir malir",spil[8])
        veldu=int(input("Veldu flokk "))
        print("tölvann dróg spilið",spil2[0],"1. Þyngd",spil2[1],"2. Mjólkurlagni dætra",spil2[2],"3. Einkunn ullar",spil2[3],"4. Fjöldi afkvæma",spil2[4],"5. Einkunn læris",spil2[5],"6. Frjósemi",spil2[6],"7. Gerð/þykkt bakvöðva",spil2[7],"8. Einkunn fyrir malir",spil2[8])
    if teljari%2!=0:
        print("tölvann dróg spilið",spil2[0],"1. Þyngd",spil2[1],"2. Mjólkurlagni dætra",spil2[2],"3. Einkunn ullar",spil2[3],"4. Fjöldi afkvæma",spil2[4],"5. Einkunn læris",spil2[5],"6. Frjósemi",spil2[6],"7. Gerð/þykkt bakvöðva",spil2[7],"8. Einkunn fyrir malir",spil2[8])
        randomtala=randint(1,8)
        print("Tölvann valdi ",randomtala)
        print("Þú drókst spilið",spil[0],"1. Þyngd",spil[1],"2. Mjólkurlagni dætra",spil[2],"3. Einkunn ullar",spil[3],"4. Fjöldi afkvæma",spil[4],"5. Einkunn læris",spil[5],"6. Frjósemi",spil[6],"7. Gerð/þykkt bakvöðva",spil[7],"8. Einkunn fyrir malir",spil[8])
    utkoma=float(spil[veldu])-float(spil2[veldu])


    if utkoma>0:
        print("Spilari vann")
        spilari.append(tolva[0])
        tolva.remove(tolva[0])
        spilari.append(spilari[0])
        spilari.remove(spilari[0])
        if len(strid)>0:
            for x in strid:
                spilari.append(x)
            strid=[]
    elif utkoma<0:
        print("Tolva vann")
        tolva.append(spilari[0])
        spilari.remove(spilari[0])
        tolva.append(tolva[0])
        tolva.remove(tolva[0])
        if len(strid)>0:
            for x in strid:
                spilari.append(x)
            strid=[]
    elif utkoma==0:
        print("Jafntefli")
        strid.append(tolva[0])
        tolva.remove(tolva[0])
        strid.append(spilari[0])
        spilari.remove(spilari[0])
    teljari+=1
    print("Spilari er með", len(spilari), "talvan er með", len(tolva))
if len(tolva)==0:
    print("Spilari vann spilið")
if len(spilari)==0:
    print("Tolvan vann spilið")