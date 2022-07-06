
#TODO Creer un bus
import copy
bus_model = {
    'id': '',
    'seat': 0,
    'passengers' : []
}

buses = []

def create_bus():
    seat = int(input("Place: "))
    matricule = input("Matricule du bus: ")
    check_matricule = check_if_matricule_is_used(matricule)

    if check_matricule:
        while(check_matricule):
            matricule = input("Matricule du bus: ")
            check_matricule = check_if_matricule_is_used(matricule)
        return generate_bus(matricule, seat)

    return generate_bus(matricule, seat)
        

def generate_bus(matricule, seat):
    new_bus = copy.deepcopy(bus_model)
    new_bus['id'] = matricule
    new_bus['seat'] = seat
    buses.append(new_bus)
    return new_bus

def check_if_matricule_is_used(matricule):
    for bus in buses:
        if bus['id'] == matricule:
            return True

    return False


busA = create_bus()
busB = create_bus()
print(busA, busB)


