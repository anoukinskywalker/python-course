import math

# En mathématiques, la suite de Fibonacci est une suite d'entiers dans laquelle
# chaque terme est la somme des deux termes qui le précèdent (Wikipédia).

# En voici le début :
# 0, 1, 1, 2, 3, 5, 8...

# Écrivez une fonction find_in_fibonacci_suite()
# Cette fonction prendra un tableau d'entiers.
# La fonction doit retourner le premier entier de la liste qui appartient à la
# suite de Fibonacci (ou 0 si aucun ne correspond).

################################################################################
def find_in_fibonacci_suite(tab) :
    noFib=0
    for t in tab :
        f1=5*pow(t,2)+4
        f2=5*pow(t,2)-4
        if (math.sqrt(f1).is_integer() or math.sqrt(f2).is_integer() ):
            return t
        else :
            noFib=0
    return noFib           
################################################################################



































print('\033[92m✓ OK' if find_in_fibonacci_suite([1, 15, 75]) == 1 and find_in_fibonacci_suite([584, 987, 2]) == 987 and find_in_fibonacci_suite([144, 50, 89]) == 144 and find_in_fibonacci_suite([16, 87, 154]) == 0 else '\033[91m❌KO')
