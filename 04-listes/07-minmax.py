# Il est assez simple de deviner à quoi servent min() et max() sur une liste !

# Créez une variable "max_note" qui contiendra la meilleure note de toutes les
# notes obtenues par Jane et John.

################################################################################
jane_notes = [14, 8, 19, 8, 15]
john_notes = [8, 4, 20, 17, 8]
################################################################################

max_note=max([max(jane_notes), max(john_notes)])
# Vous pouvez utilisez deux variables intermédiaires, mais il est possible de 
# le faire en une seule ligne de plusieurs façons, essayez de trouver comment.



































print('\033[92m✓ OK' if max_note == 20 else '\033[91m❌KO')
