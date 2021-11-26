# Créez une fonction "compute_notes" prenant en paramètre une liste de notes
# et un index : compute_notes([16, 13, 9, 12], 2)

# L'index représente la séparation entre le premier et le second semestre.
# Dans l'exemple, 16 et 13 sont les notes du premier semestre.

# Si l'index ne permet pas de séparer correctement le tableau, la fonction
# retourne un tableau vide.

# Le but de cette fonction est de faire ne sorte qu'un étudiant n'ait pas un
# semestre ne contenant que des zéros.

# Si un des deux semestres ne contient pas d'autre note que des zéros, on 
# rajoute à ce semestre une unique note : la plus basse (sans compter les
# zéros !) de l'autre semestre. On renvoit ensuite le tableau des notes modifié.

# Si aucun des deux semestres n'est concerné, on retourne le tableau sans 
# modification.

# Si les deux semestres ne contiennent que des zéros, on retourne le tableau
# sans modification.

# Exemple : compute_notes([16, 13, 9, 0, 0], 3) -> [16, 13, 9, 0, 0, 9]

################################################################################
def compute_notes(notes, i) :
    if (max(notes)==0) :
        return notes
    elif (i > (len(notes)-1)) :
        return []
    else :
        s1=notes[:i]
        s2=notes[i:]
        if(max(s2)==0) :
            notes.append(min(s1))
        elif(max(s1)==0) :
            notes.insert(i, min(s2))
        return notes

print(compute_notes([16, 13, 9, 0, 0], 3))
print(compute_notes([10, 12, 8], 3))
print(compute_notes([10, 8, 9, 15, 0], 4))
print(compute_notes([0, 0], 1))
print(compute_notes([0, 0, 3], 2))
print(compute_notes([0, 10, 8], 1))
################################################################################
































print('\033[92m✓ OK' if compute_notes([10, 12, 8], 3) == [] and compute_notes([10, 8, 9, 15, 0], 4) == [10, 8, 9, 15, 0, 8] and compute_notes([0, 10, 8], 1) == [0, 8, 10, 8] and compute_notes([0, 0], 1) == [0, 0] and compute_notes([0, 0, 3], 2) == [0, 0, 3, 3] else '\033[91m❌KO')
