# Il est pratiquement toujours nécessaire de vérifier que l'utilisateur a bien 
# entré une donnée dans le format attendu.

# En utilisant la boucle "while True" vue précédemment, demandez son âge à
# l'utilisateur. Si la donnée rentrée n'est pas valide (entier positif
# inférieur à 130), demandez à nouveau, jusqu'à ce qu'elle le soit.

# Pas de correction automatique pour cet exercice.

################################################################################
while True :
    print("Quel est votre age?")
    age=input()
    if (int(age) < 130) :
        break
################################################################################