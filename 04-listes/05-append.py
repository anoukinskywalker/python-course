# Les fonctions append et insert permettent d'injecter de nouvelles valeurs 
# dans une liste.

# La fonction append ajoute toujours à la fin du tableau
# [1, 2, 3].append(4) -> [1, 2, 3, 4]

# La fonction insert permet de spécifier l'index auquel on souhaite faire l'ajout
# [1, 2, 3].insert(3, 4) -> [1, 2, 3, 4]

# Il manque deux voyelles dans le tableau, à vous de les ajouter !

################################################################################
voyels: list[str] = ['E', 'I', 'O', 'U']
################################################################################

voyels.append('Y')
voyels.insert(0, 'A')


































print('\033[92m✓ OK' if voyels == ["A", "E", "I", "O", "U", "Y"] else '\033[91m❌KO')
