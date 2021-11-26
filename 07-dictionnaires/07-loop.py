# Il peut être utile de parcourir un dictionnaire pour tester ou effectuer
# une opération sur chacune de ses valeurs.

# L'écriture de la boucle est de type
# for key in list.keys():
# Où list est le dictionnaire.
# Vous pouvez remplacer key par le nom que vous voulez : utilisez
# des noms explicites !
# Ensuite, vous pouvez accéder aux valeurs en utilisant list[key]

# Trouvez la note la plus élevée du dictionnaire "notes" et stockez le nom de la
# matière associée dans une variable best_course

from typing import TypedDict

class Notes(TypedDict):
    math: int
    french: int
    english: int

notes: Notes = {
    "math": 8,
    "french": 15,
    "english": 20
}

################################################################################
best_course: str = ''
best_note=0
for course in notes.keys():
    if (notes[course]>=best_note) :  
        best_note=notes[course]
        best_course = course

################################################################################





































print('\033[92m✓ OK' if best_course == "english" else '\033[91m❌KO')
