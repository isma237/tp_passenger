import copy
busModel = {
    "id": "",
    "place_available": 0,
    "passengers" : []
}

passengerModel = {
    "id": "",
    "name": "",
    "weight" : 0
}

allPassengers = []
allBuses = []

#Création d'un bus
def createBus(id, nombre_place):
    currentBus = copy.deepcopy(busModel)
    currentBus['id'] = id
    currentBus['place_available'] = nombre_place
    allBuses.append(currentBus)
    return currentBus

#Création d'un passager
def createPassenger(id, name, weight):
    if (checkIfUserNotExist(id, allPassengers)):
        currentPassenger = copy.deepcopy(passengerModel)
        currentPassenger['id'] = id
        currentPassenger['name'] = name
        currentPassenger['weight'] = weight

        allPassengers.append(currentPassenger)

    return currentPassenger


def checkIfUserNotExist(identifiant, table):
    for item in table:
        if item['id'] == identifiant:
            return False

    return True


lt545 = createBus("LT545", 50)
lt530 = createBus("LT530", 5)
lt500 = createBus("LT500", 50)

hawaou = createPassenger("696273789", "Hawaou", 22)
morelle = createPassenger("694412340", "Morelle", 20)

def getAvailablePlaces(bus):
    return bus['place_available'] - len(bus['passengers'])

def isPlaceAvailable(bus):
    if getAvailablePlaces(bus) > 0:
        return True
    else: 
        return False


def addPassengerInBus(passenger, bus):
    state = isPlaceAvailable(bus)
    if state == True:
        bus['passengers'].append(passenger)
    else:
        print("Nous n'avons plus de place disponible")

def removePassengerInBus(bus, passenger):
    if(not checkIfUserNotExist(passenger['id'], bus['passengers'])):
        bus['passengers'].remove(passenger)


addPassengerInBus(hawaou, lt530)
addPassengerInBus(morelle, lt530)

def listPassengerInBus(bus):      
    passengers = bus["passengers"]
    for passenger in passengers:
        print(passenger["name"])
   
listPassengerInBus(lt530)

def getTotalWeightInBus(bus):
    passengers = bus['passengers']
    totalWeight = 0
    for passenger in passengers :
        totalWeight = totalWeight + passenger['weight']

    return totalWeight

total = getTotalWeightInBus(lt530)

def checkIfPassengerPresentInBus(identifiant):
    exist = False
    for bus in  allBuses:
        for passenger in bus['passengers']:
            if passenger['id'] == identifiant:
                exist = True
                print(passenger)
                print(bus)
                break
        if exist:
            break

checkIfPassengerPresentInBus("696273789")