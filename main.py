#---------------------------------TEMPLATES------------------------------------------------
#my passenger template
import copy


passengerTemp = {
    "name" : " ",
    "id" : "busID+numeroSiege",
    "lgageWeight" : 0.0
}

#my Bus template
busTemp = {
    "id" : "",
    "availablePlace" : 0,
    "nbreKg":0.0,
    "listPassenger" : []
}

myListBus = []
myVacanPassgerList = []
response="m"
#---------------------------------FONCTIONS DEFINITION--------------------------------
def createBus(): #creation d'un bus
    response=''
    print("___________Creer un nouveau bus___________")
    while response != 'n':
        print()
        currentBus = copy.deepcopy(busTemp)
        currentBus["id"] = input("==> Entrer l'ID du bus :  ").lower()
        for bus in myListBus:
            while bus["id"]==currentBus["id"]:
                print("    un autre bus a deja le meme ID")
                currentBus["id"]=input("    Entrer l'ID du bus :  ").lower()
        currentBus["availablePlace"] = int(input("    Entrer le nombre de siege :  "))
        myListBus.append(currentBus)
        response = input("creer un autre bus ?  y/n___  ")
        while response != 'n' and response != 'y':
            response = input("creer un autre bus ?  y:yes or n:no___  ")
        print("------------------------------------------------------------")
    
def createPassenger(): #creation d'un passager
    
    response = ''
    id=0
    print("___________Creer un nouveau passager__________")
    while response != 'n':
        print()
        currentPassenger = copy.deepcopy(passengerTemp)
        currentPassenger["name"] = input("==> Entrer son nom :  ").lower()
        for char in currentPassenger["name"]:
            id += ord(char)
        currentPassenger["id"] =str(id)
        currentPassenger["lgageWeight"] = float(input("    Poids des bagages :  "))
        myVacanPassgerList.append(currentPassenger)
        response = input("creer un autre passager ?y/n__  ")
        print("------------------------------------------------------------")

def addPassengerInBus(passengerName , busId): #ajout d'un passager dans un bus
    response='r'
    status=0
    curentbus={}

    for bus in myListBus:
        if busId == bus["id"]:
            curentbus=bus
        
    for pssger in myVacanPassgerList:
        if passengerName.lower() == pssger["name"]:
            if len(curentbus["listPassenger"]) < curentbus["availablePlace"]:
                curentbus["listPassenger"].append(pssger)
                pssger["id"]=curentbus["id"] + str(curentbus["listPassenger"].index(pssger))
                curentbus["nbreKg"] += pssger["lgageWeight"]
                myVacanPassgerList.remove(pssger)
                print("==> le passager a ete ajouter avec success dans le bus")
                status=1
            else:
                status=2
    if status==0:
        print("the name entred in incorrect")
    if status==2:
        print("this bus is full ,it can't receive another passenger")

    print("------------------------------------------------------------")
            
def movePassengerInBus(passengerName , busId):

    status1=0
    status2=0
    curentbus={}
    id=0
    
    for bus in myListBus:
        if busId == bus["id"]:
            curentbus=bus
            status1=1
    for pssger in curentbus["listPassenger"]:
        if passengerName.lower() == pssger["name"]:
            curentbus["listPassenger"].remove(pssger)
            for char in pssger["name"]:
                id += ord(char)
            pssger["id"]=str(id)
            curentbus["nbreKg"] -= pssger["lgageWeight"]
            myVacanPassgerList.append(pssger)
            status2=1
    if status1 == 1 and status2 == 0:
        print("==> il n'existe pas d'utilisateur de ce nom enregistre dans ce bus")
    elif status2==0:
        print("==> le nom du passager renseigner est incorrect")
    elif status1==0:
        print("==> l'ID du bus renseigner est incorrect") 

    
def printVacanListPassger(): #liste des passager vacans
    for passger in myVacanPassgerList:
        print("==>  ID : {}   Name :  {}   Lugage weight :  {}".format(passger["id"],passger["name"].capitalize(),passger["lgageWeight"]))

def printBuspassgerList(busId):#liste des passger dans un bus specifique
    count = 0
    for bus in myListBus:
        if bus["id"] == busId:
            passengers=bus["listPassenger"]
            for passger in passengers:
                print("==>  ID : {}   Name :  {}   Lugage weight :  {}".format(passger["id"],passger["name"].capitalize(),passger["lgageWeight"]))
                count += 1
    if count == 0:
        print("==> Il n'ya aucun passager dans ce bus ")

def allBusInfo():
    print("___________Information sur tous les bus ____________")
    print()
    count = 0
    for bus in myListBus:
        print("==> ID :  {}  Possible places :  {}  Available places :  {}  number of Kg in bus :  {}".format(bus["id"],bus["availablePlace"],bus["availablePlace"] - len(bus["listPassenger"]),bus["nbreKg"]))
        for pssger in bus["listPassenger"]:
            print("        Id : {}  Name :  {}".format(pssger["id"],pssger["name"]))
            count += 1
    if count == 0 :
        print("==> vous n'avez enregistrer aucun bus pour le moment")

def BusInfo(busId):
    for bus in myListBus:
        if busId == bus["id"]:
            print("==> ID :  {}  Possible places :  {}  Available places :  {}".format(bus["id"],bus["availablePlace"],bus["availablePlace"] - len(bus["listPassenger"]),bus["nbreKg"]))
            for pssger in bus["listPassenger"]:
                print("informations sur les passagers")
                print("        Id : {}  Name :  {}  Lugage weight :  {} ".format(pssger["id"],pssger["name"],pssger["lgageWeight"]))

def verifiedPassgerInBus(passengerName):
    status=0
    thebus={}
    for bus in myListBus:
        for pssger in bus["listPassenger"]:
            if passengerName == pssger["name"]:
                status = 1
                thebus = bus
    if status == 1:
        print("==> le passager "+ passengerName +" est bien present dans ce bus ")
        BusInfo(thebus["id"])
    else:
        print("==> Ce passager est encore vacan il n'est inscrit dans aucun bus")

def verifiedTransfer(BusCommingId,BusGoingId):
    placeUseInBuscomming=0
    placeAvailableInBusGoing=0
    commingBus={}
    goingBus={}
    status=0
    for bus in myListBus:
        if BusCommingId == bus["id"]:
            commingBus = bus
            status += 1
        else:
            goingBus = bus
            status += 1
    if status == 1 or status == 0 :
        print("L'un des ID de bus renseigner est incorrect")
    else:
        placeUseInBuscomming = commingBus["availablePlace"] - len(commingBus["listPassenger"])
        placeAvailableInBusGoing = goingBus["availablePlace"] - len(goingBus["listPassenger"])

        if placeUseInBuscomming <= placeAvailableInBusGoing:
            print("==> Le transfert de passager du bus {} vers le bus {} est possible".format(BusCommingId,BusGoingId))
        else:
            print("==> Le transfert de passager du bus {} vers le bus {} est impossible".format(BusCommingId,BusGoingId))

def myswitcher(choix):

    if choix == "a":
        createBus()
    elif choix == "b":
        createPassenger()
    elif choix == "c":
        #allBusInfo()
        response="r"
        
        print()
        print("______________Tous les bus enregistree_______________")
        print()
        while response =="r":
            for bus in myListBus:
                print("==> ID :  {}  Possible places :  {}  Available places :  {}  number of Kg in bus :  {}".format(bus["id"],bus["availablePlace"],bus["availablePlace"] - len(bus["listPassenger"]),bus["nbreKg"]))
            print()
            id = input("==> Entrer l'id du bus :  ")
            print()
            print("______________Tous les passagers vacans_______________")
            print()
            printVacanListPassger()
            name = input("==> Entrer le nom du passager a ajouter :  ")
            addPassengerInBus(name,id)
            response = input("Entrer r pour ajouter un autre passager et tout autre lettre pou sortir__:  ")
    elif choix == "d":
        #allBusInfo()
        response="r"
        print()
        print("______________Tous les bus enregistree_______________")
        print()
        while response =="r":
            for bus in myListBus:
                print("==> ID :  {}  Possible places :  {}  Available places :  {}  number of Kg in bus :  {}".format(bus["id"],bus["availablePlace"],bus["availablePlace"] - len(bus["listPassenger"]),bus["nbreKg"]))
            print()
            id = input("==> Entrer l'id du bus :  ")
            print()
            print("______________Tous les passagers de ce bus_______________")
            print()
            printBuspassgerList(id)
            name = input("==> Entrer le nom du passager a retirer :  ")
            movePassengerInBus(name,id)
            response = input("Entrer r pour ajouter un autre passager et tout autre lettre pou sortir__:  ")
    elif choix == "e":
        printVacanListPassger()
    elif choix == "f":
        #allBusInfo()
        print()
        print("______________Tous les bus enregistree_______________")
        print()
        for bus in myListBus:
            print("==> ID :  {}  Possible places :  {}  Available places :  {}  number of Kg in bus :  {}".format(bus["id"],bus["availablePlace"],bus["availablePlace"] - len(bus["listPassenger"]),bus["nbreKg"]))
        print()
        id = input("==> Entrer l'id du bus :  ")
        printBuspassgerList(id)
    elif choix == "g":
        name = input("==> Entrer le nom complet du passager :  ")
        verifiedPassgerInBus(name)
    elif choix == "h":
        allBusInfo()
    elif choix == "i":
        for bus in myListBus:
            print("==> ID :  {}  Possible places :  {}  Available places :  {}  number of Kg in bus :  {}".format(bus["id"],bus["availablePlace"],bus["availablePlace"] - len(bus["listPassenger"]),bus["nbreKg"]))
        print()
        idcomming = input("==> Entrer l'id du bus de provenance :  ")
        idgoing = input("==> Entrer l'id du bus de destiation:  ")
        verifiedTransfer(idcomming,idgoing)


    



#---------------------------------MAIN------------------------------------------------

choix = ""
while response == "m":
    print("----------------------GESTION DES PASSAGERS----------------------------")
    print()
    print(">     ENTRER \"A\" CREER D'UN BUS")
    print(">     ENTRER \"B\" CREER UN PASSAGER")
    print(">     ENTRER \"C\" AJOUTER UN PASSAGER DANS UN BUS")
    print(">     ENTRER \"D\" RETIRER UN PASSAGER D'UN BUS")
    print(">     ENTRER \"E\" AFFICHER LA LISTE DE TOUS LES PASSAGERS VACANS ")
    print(">     ENTRER \"F\" AFFICHER LA LISTE DE TOUS LES PASSAGERS D'UN BUS")
    print(">     ENTRER \"G\" VERIFIER SI UN PASSAGER EST ENREGISTRER DANS UN BUS")
    print(">     ENTRER \"H\" INFORMATIONS SUR TOUS LES BUS CREER")
    print(">     ENTRER \"I\" VERIFIER LE TRANSFER DE PASSAGER D'UN BUS A UN AUTRE")
    print()
    choix = input("==>   Enter votre choix___:  ")

    myswitcher(choix.lower())
    response = input("==> Taper \"M\" pour rentrer au menu et tous autre caractere pour sortie du programme__:  ").lower()


#---------------------------------MAIN------------------------------------------------
