# Une chaîne est un tableau de caractères. Les mêmes opérations sont donc 
# possibles que sur une liste !

# Créez une fonction is_valid_time() qui prend en paramètre un temps au format
# "HH:mm" et qui retourne True si le format est valide et si l'heure existe.

################################################################################
def is_valid_time(time) :
    t=time.split(":")
    if (len(time)==5):
        if (t[0].isnumeric() and t[1].isnumeric()) :
            return ((int(t[0]) >= 0 and int(t[0]) < 24) and (int(t[1])>=0 and int(t[1]) <60))

################################################################################





































print('\033[92m✓ OK' if is_valid_time('23:59') and is_valid_time('00:00') and not is_valid_time('2:4') and not is_valid_time('25:00') and not is_valid_time('ab:cd') else '\033[91m❌KO')

