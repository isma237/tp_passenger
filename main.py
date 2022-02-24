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
    "listPassenger" : []
}

myListBus = []
myVacanPassgerList = []
#---------------------------------FONCTIONS DEFINITION--------------------------------
def createBus(): #creation d'un bus
    response=''
    print("___Create a new Bus___")
    while response != 'n':

        currentBus = copy.deepcopy(busTemp)
        currentBus["id"] = input("==> Enter the bus ID :  ")
        for bus in myListBus:
            while bus["id"]==currentBus["id"]:
                print("another bus has already the same ID")
                currentBus["id"]=input("    Enter the bus ID:  ")
        currentBus["availablePlace"] = int(input("    Enter the possible seat :  "))
        myListBus.append(currentBus)
        response = input("create another bus ? y/n___  ")
        while response != 'n' and response != 'y':
            response = input("create another bus ? y:yes or n:no___  ")
        print("------------------------------------------------------------")
    
def createPassenger(): #creation d'un passager
    
    response = ''
    id=0
    print("___Create a new Passenger___")
    while response != 'n':
        
        currentPassenger = copy.deepcopy(passengerTemp)
        currentPassenger["name"] = input("==> Entrer his name :  ").lower()
        for char in currentPassenger["name"]:
            id += ord(char)
        currentPassenger["id"] =str(id)
        currentPassenger["lgageWeight"] = float(input("    Lugage weight :  "))
        myVacanPassgerList.append(currentPassenger)
        response = input("create anaother passenger ?y/n__  ")
        print("------------------------------------------------------------")

def addPassengerInBus(passengerName , busId): #ajout d'un passager dans un bus
    response='r'
    status=0
    curentbus={}
    while response == "r": 
        for bus in myListBus:
            if busId == bus["id"]:
                curentbus=bus
            
        for pssger in myVacanPassgerList:
            print(pssger)
            if passengerName.lower() == pssger["name"]:
                curentbus["listPassenger"].append(pssger)
                pssger["id"]=curentbus["id"] + str(curentbus["listPassenger"].index(pssger))
                myVacanPassgerList.remove(pssger)
                status=1
        if status==0:
            print("the name entred in incorrect")

        response=input("Enter the letter R to retry  :  ")
        print("------------------------------------------------------------")
            

def movePassengerInBus(passengerName , busId):
    response='r'
    status1=0
    status2=0
    curentbus={}
    while response == 'r': 
        for bus in myListBus:
            if busId == bus["id"]:
                curentbus=bus
                status1=1
        for pssger in curentbus["listPassenger"]:
            if passengerName.lower() == pssger["name"]:
                curentbus["listPassenger"].remove(pssger)
                myVacanPassgerList.append(pssger)
                status2=1
        if status2==0:
            print("the name entred in incorrect")
        if status1==0:
            print("the bus id entred in incorrect") 

        response=input("Entrer la lettre R pour reessayer :  ")
    

def printVacanListPassger(): #liste des passager vacans
    for passger in myVacanPassgerList:
        print("==>  ID : {}   Name :  {}   Lugage weight :  {}".format(passger["id"],passger["name"].capitalize(),passger["lgageWeight"]))

def printBuspassgerList(busId):#liste des passger dans un bus specifique
    for bus in myListBus:
        if bus["id"] == busId:
            passengers=bus["listPassenger"]
            for passger in passengers:
                print("==>  ID : {}   Name :  {}   Lugage weight :  {}".format(passger["id"],passger["name"].capitalize(),passger["lgageWeight"]))


#---------------------------------MAIN------------------------------------------------
createBus()
createPassenger()
print(myListBus)
printVacanListPassger()
busId=input("enter l'id du bus   ")
passger=input("enter entrer le nom du passager   ")
print("1------------------------------------------------------------")
addPassengerInBus(passger,busId)
print("2------------------------------------------------------------")
printBuspassgerList(busId)
print("3------------------------------------------------------------")
printVacanListPassger()
print("4------------------------------------------------------------")
movePassengerInBus(passger,busId)
printBuspassgerList(busId)
print("5------------------------------------------------------------")
printVacanListPassger()



















#---------------------------------MAIN------------------------------------------------
