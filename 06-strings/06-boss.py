# Créez une fonction is_valid_password() qui prend en paramètre une chaîne de
# caractère et qui vérifie si le mot de passe est valide selon les critères
# suivants :

# Le mot de passe fait au moins 6 caractères
# Il contient au moins une lettre minuscule
# Il contient au moins une lettre majuscule
# Il contient au moins deux chiffres
# Il ne contient pas d'autre type de caractère (car notre base de données ne sait pas les gérer)

# La fonction doit renvoyer un booléen.

################################################################################
def is_valid_password(password) :
    nchiffre=0
    nMaj=0
    nMin=0
    pcharacters=list(password)
    for char in pcharacters :
        if char.isnumeric() :
            nchiffre=nchiffre+1
        elif char.isupper() :
            nMaj=nMaj+1
        elif char.islower() :
            nMin=nMin+1
        else :
            return False
    print(nchiffre>=2 and nMaj>=1 and len(password) >=6)
    return (nchiffre>=2 and nMaj>=1 and len(password) >=6 and nMin >=1)
        
################################################################################

# Pour simplifier vos test, utilisez input() et "while True" afin de pouvoir
# tester plusieurs entrées d'affilée.















































print('\033[92m✓ OK' if is_valid_password('1E4a2E') and not is_valid_password('1E8a2') and not is_valid_password('1EDA2E') and not is_valid_password('1eda2e') and not is_valid_password('sedEfe') and not is_valid_password('sedEf!') and not is_valid_password('sedEf7') else '\033[91m❌KO')
