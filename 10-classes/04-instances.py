# À partir d'une classe, on peut créer autant d'instances que l'on souhaite,
# chacune est un objet séparé. Ces objets peuvent être manipulés comme des
# variables (à vrai dire, ce sont des variables !).

# Reprenez votre classe User.

# En dehors de la classe, créez une fonction get_oldest(). Cette fonction doit
# prendre deux instances de la classe User en paramètre, et renvoyer le
# fullname (prénom + nom) de l'utilisateur le plus vieux
# (on ignore le cas où les âges sont égaux).

################################################################################
class User :
    def __init__(self, fn, ln, age):
        self.firstname = fn
        self.lastname = ln
        self.age = age
        self.followers = 0
    
    def is_adult(self) :
        if (self.age >= 18 ) :
            return True
        else :
            return False
    
    def get_full_name(self) :
        return self.firstname + " " + self.lastname

    def add_followers(self, n):
        if (self.is_adult()) :
            self.followers = self.followers +n

def get_oldest(user1, user2) :
    if (user1.age > user2.age) :
        return user1.get_full_name()
    else :
        return user2.get_full_name()

bob = User("Bob", "Doe", 18)
################################################################################

# N'oubliez pas le typage. Une classe est également un type, ce qui est bien
# pratique.
















test_adult = User("bob", "doe", 18)
test_child = User("child", "doe", 10)
print('\033[92m✓ OK' if get_oldest(test_adult, test_child) == "bob doe" else '\033[91m❌KO')