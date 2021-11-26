# Les fonctions remove et pop permettent de retirer des valeurs d'un tableau.

# Remove retire la première valeur correspondante trouvée :
# [7, 8, 8, 9].remove(8) -> [7, 8, 9]

# pop permet de retirer une valeur en fonction de son index :
# [7, 8, 8, 9].pop(1) -> [7, 8, 9]

# Retirez les éléments intrus dans le tableau des voyelles

################################################################################
voyels: list[str] = ['A', 'E', 'X', 'I', 'O', 'X', 'U', 'Y']
################################################################################

voyels.remove('X')
voyels.pop(4)
# Non, il n'existe pas de méthode removeAll() en python... (mais d'autres 
# astuces sont envisageables)








































print('\033[92m✓ OK' if voyels == ["A", "E", "I", "O", "U", "Y"] else '\033[91m❌KO')
