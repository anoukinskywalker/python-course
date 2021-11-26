# Les types peuvent hériter les uns des autres. Si cela ne vous dit pas grand
# chose, considérez l'exemple suivant :

# Un véhicule possède un nombre de places et un coût.

# Une voiture est un véhicule. Elle possède en effet un nombre de places et un
# coût. Elle possède en plus des caractéristiques qui lui sont propres : un
# nombre de portes et un kilométrage.

# Un train est aussi un véhicule, qui possède donc un nombre de places et un
# coût. Il possède d'autres caractéristiques propres : un nombre de
# wagons (wagons_count) et la présence ou non d'un wagon bar (has_bar_wagon)

# Le code ci-dessous implémente les types Vehicle et Car. Ajoutez le type Train.
# Créez des variables my_car et my_train qui utilisent les types appropriés.

from typing import TypedDict

class Vehicle(TypedDict):
    seats: int
    cost: int

class Car(Vehicle):
    doors_count: int
    kilometers: int

################################################################################
class Train(Vehicle):
    wagons_count: int
    has_bar_wagon: bool

my_car : Car = {
    "seats" : 5,
    "cost" : 10000,
    "doors_count" : 4,
    "kilometers" : 100000
}

my_train : Train = {
    "seats" : 500,
    "cost" : 10000000,
    "wagons_count" : 20,
    "has_bar_wagon" : True,
}
################################################################################

# Pas de validation automatique pour cet exercice. Encore une fois, vérifiez
# bien que python détecte correctement les types.

# Dans certains langages, le type Vehicle serait appelé un type abstrait : il 
# n'est pas censé être utilisé directement et ne sert que de base à d'autres
# types.

# Les types peuvent hériter les uns des autres à l'infini ! 
# Par exemple, un type ElectricCar pourrait hériter du type Car.



























