# Un troisième "paramètre" peut être ajouté lorsqu'on accède aux éléments d'un
# tableau pour créer un sous-tableau. Il s'agit de l'incrément (step).

# Exemple : [1, 2, 3, 4, 5, 6, 7, 8, 9][1:6:3]
# Tous les éléments entre l'index 1 (inclus) et 6 (non-inclus), avec un écart de
# 2 entre chaque. Ce qui donne [2, 5]

# En utilisant le tableau "months", créez un tableau "odd_months" qui stocke
# tout les mois pairs ("Feb", "Apr", "May"...)

################################################################################
months: list[str] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
################################################################################

odd_months=months[1:12:2]
print(odd_months)
# Conseil : Passez vous des paramètres optionnel. Seuls deux chiffres sont ici
# nécessaire entre les crochets, mais vous devrez peut-être consulter la
# documentation pour trouver la bonne syntaxe.

# odd = impair
# even = pair








































print('\033[92m✓ OK' if odd_months == ["Feb", "Apr", "Jun", "Aug", "Oct", "Dec"] else '\033[91m❌KO')
