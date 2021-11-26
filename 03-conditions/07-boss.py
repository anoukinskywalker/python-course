# Créez une fonction is_leap_year qui prend une année en paramètre. Elle doit
# renvoyer True si l'année est bissextile, False sinon.

# Pour vérifier qu'un nombre est divisible par 4, il faut utiliser l'opération
# modulo. Cette opération donne le reste de la division par 0. Donc si le modulo
# vaut 0, cela veut dire que le nombre est divisible.

# 12 % 4 = 0 (il n'y a pas de reste car 12 est divisible par 4)
# 13 % 4 = 1 (il y a un reste : 13 n'est pas divisible par 4)

################################################################################
def is_leap_year(year : int) :
    return ((year%4 == 0 and year%100!=0) or (year%100==0 and year%400==0))
################################################################################

print(is_leap_year(2000))
print(is_leap_year(1900))
print(is_leap_year(1998))
print(is_leap_year(2004))


























print('\033[92m✓ OK' if is_leap_year(2000) and not is_leap_year(1900) and not is_leap_year(1998) and is_leap_year(2004) else '\033[91m❌KO')
