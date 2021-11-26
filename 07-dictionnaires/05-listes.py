# Une liste peut contenir des dictionnaires, et un dictionnaire peut contenir
# des listes !

# Creéz une tableau "students" qui contiendra 3 dictionnaire de type "Student" 
# que vous aurez créé. Typez bien le tableau pour qu'il ne puisse contenir que
# des dictionnaires de type "Student".

from typing import TypedDict

class Student(TypedDict):
    firstname: str
    lastname: str
    notes: list[int]

################################################################################

student1 : Student = {
    "firstname" : "yo",
    "lastname" : "yo",
    "notes" : [1,2,3]
}

student2 : Student = {
    "firstname" : "yo",
    "lastname" : "yo",
    "notes" : [1,2,3]
}

student3 : Student = {
    "firstname" : "yo",
    "lastname" : "yo",
    "notes" : [1,2,3]
}

students = []
students.append(student1)
students.append(student2)
students.append(student3)

################################################################################






































print('\033[92m✓ OK' if len(students) == 3 else '\033[91m❌KO')
