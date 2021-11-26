# Une opération utile est de trouver l'index d'une valeur dans un tableau. C'est
# ce que permet la fonction index.

# [1, 2, 3].index(1) -> 0

# Grâce à la liste "month" et la fonction index(), créez une variable "message" contenant le texte :
# "Mars est le 3e mois de l'année"

################################################################################
months: list[str] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
################################################################################

message="Mars est le " + str(months.index("Mar")+1) + "e mois de l'année"
print(message)








































print('\033[92m✓ OK' if message == "Mars est le 3e mois de l'année" else '\033[91m❌KO')
