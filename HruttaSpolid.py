#Bergþór Ingi Birgirsson
#+ hjálpaði mér vin minn í
#basicly Importar Random
from random import *
#þetta opnar spil2 text File að spil
with open("spil2.txt","r") as spil:
    #þetta er spilastokkur fagið það les og splittar og skrifar í eina línu
    spilastokkur=spil.read().split("\n")
#þetta lokar spil fagið
spil.close()
#þetta er listar fyrir spilarana og tölvu
spilari=[]
tolva=[]
#þessi lykkja velur random spil og removar spil frá spilastokk og finnur lengd spil og ef það er 26 þá stoppar
for x in spilastokkur:
    randomtala=randint(0,len(spilastokkur)-1)
    spilari.append(spilastokkur[randomtala])
    spilastokkur.remove(spilastokkur[randomtala])
    if len(spilari)==26:
        break
#talvan er í spilastokk
tolva=spilastokkur
#þetta gerir list fyrir stríð
strid=[]
#þetta er telur núll
teljari=0
#þegar lengd spilara er 0 og lengd tölva hefur 0
while len(spilari)!=0 and len(tolva)!=0:
    #þessi liðiur er seigir að spil og spil2 er breytt spilari[0] og splittar bæði með ","
    spil=str(spilari[0])
    spil=spil.split(",")
    spil2=str(tolva[0])
    spil2=spil2.split(",")
    #þetta fer ef teljari er 0
    if teljari%2==0:
        #þetta prentar út alla möguleikanna og að þú getur valið fyrir stríðið
        print("Þú drókst spilið",spil[0],"1. Þyngd",spil[1],"2. Mjólkurlagni dætra",spil[2],"3. Einkunn ullar",spil[3],"4. Fjöldi afkvæma",spil[4],"5. Einkunn læris",spil[5],"6. Frjósemi",spil[6],"7. Gerð/þykkt bakvöðva",spil[7],"8. Einkunn fyrir malir",spil[8])
        #lætur þig velja flokk 1 ,2 ,3, 4, 5....
        veldu=int(input("Veldu flokk "))
        #þetta lætur tölvunna velja flokk
        print("tölvann dróg spilið",spil2[0],"1. Þyngd",spil2[1],"2. Mjólkurlagni dætra",spil2[2],"3. Einkunn ullar",spil2[3],"4. Fjöldi afkvæma",spil2[4],"5. Einkunn læris",spil2[5],"6. Frjósemi",spil2[6],"7. Gerð/þykkt bakvöðva",spil2[7],"8. Einkunn fyrir malir",spil2[8])

    #þetta fer ef teljari er 0
    if teljari%2!=0:
        #lætur tölvunna randomly velja
        print("tölvann dróg spilið",spil2[0],"1. Þyngd",spil2[1],"2. Mjólkurlagni dætra",spil2[2],"3. Einkunn ullar",spil2[3],"4. Fjöldi afkvæma",spil2[4],"5. Einkunn læris",spil2[5],"6. Frjósemi",spil2[6],"7. Gerð/þykkt bakvöðva",spil2[7],"8. Einkunn fyrir malir",spil2[8])
        randomtala=randint(1,8)
        #prentar tölvann valdi ....
        print("Tölvann valdi ",randomtala)
        #þetta prentar út þú dróksts spilið .... svo veluru flokk
        print("Þú drókst spilið",spil[0],"1. Þyngd",spil[1],"2. Mjólkurlagni dætra",spil[2],"3. Einkunn ullar",spil[3],"4. Fjöldi afkvæma",spil[4],"5. Einkunn læris",spil[5],"6. Frjósemi",spil[6],"7. Gerð/þykkt bakvöðva",spil[7],"8. Einkunn fyrir malir",spil[8])
    utkoma=float(spil[veldu])-float(spil2[veldu])

    #ef útkomann er 0 þá vinnur þú
    if utkoma>0:
        print("Spilari vann")
        #þetta addar inní lista og .remove removar það
        spilari.append(tolva[0])
        tolva.remove(tolva[0])
        #þetta addar inna spilari
        spilari.append(spilari[0])
        spilari.remove(spilari[0])
        #ef lengin á striðinnu er 0 þá ...
        if len(strid)>0:
            #þetta addar stríðinnu inná spilara
            for x in strid:
                spilari.append(x)
                #þetta býr til lista strid
            strid=[]
    #ef utkoman er lægri en núll
    elif utkoma<0:
        #þetta prentar út tolva vann
        print("Tolva vann")
        #þetta addar stigunum inna spilara og drasl
        tolva.append(spilari[0])
        spilari.remove(spilari[0])
        tolva.append(tolva[0])
        tolva.remove(tolva[0])
        if len(strid)>0:
            for x in strid:
                spilari.append(x)
            strid=[]
    #ef utkomann er 0 þá bara janftefli og draslið fyrir neðan removar og addar drasli
    elif utkoma==0:
        print("Jafntefli")
        strid.append(tolva[0])
        tolva.remove(tolva[0])
        strid.append(spilari[0])
        spilari.remove(spilari[0])
    teljari+=1
    print("Spilari er með", len(spilari), "talvan er með", len(tolva))
#ef lengd tölvu er 0 þá spilarinn vinnur
if len(tolva)==0:
    print("Spilari vann spilið")
#ef lengd tölvu er 0 þá talvan vinnur
if len(spilari)==0:
    print("Tolvan vann spilið")