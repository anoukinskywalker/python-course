# L'instruction "if" est très importante : elle permet d'exécuter une partie du
# code uniquement si une condition est vérifiée

# Dans l'exemple ci-dessous, on affiche un message en fonction d'un booléen.

# Créez une fonction get_rectangle_surface qui prend en paramètre une largeur
# "width" et une hauteur "height" pour retourner une surface

# Avant de retourner la surface, dans la fonction, essayez de deviner s'il
# s'agit d'un carré. Si oui, affichez "C'est un carré !".

# Vérifiez bien par vous-même que le message s'affiche.

################################################################################
first_visit: bool = True

if first_visit:
    print('Welcome !')
################################################################################
def get_rectangle_surface(longueur: int, largeur : int) :
    surface=longueur*largeur
    if(longueur==largeur) :
        print("c'est un carré!")
    return surface

print(get_rectangle_surface(4, 6))
























print('\033[92m✓ OK' if get_rectangle_surface(8, 4) == 32 else '\033[91m❌KO')
