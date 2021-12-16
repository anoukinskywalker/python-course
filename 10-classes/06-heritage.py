# Un point crucial concernant les classes est la notion d'héritage (comme
# pour les types !)

# Voici un exemple :

class MyClass:
    def __init__(self, letter: str):
        self.letter = letter

    def get_letter(self):
        return self.letter

class MySubClass(MyClass):
    def __init__(self, letter: str, number: int):
        MyClass.__init__(self, letter)
        self.number = number

    def get_number(self):
        return self.number

my_instance = MySubClass("a", 2)
print(my_instance.get_letter())
print(my_instance.get_number())

# Prenez bien le temps de comprendre ce qui se passe !
# MyClass possède un attribut letter et une méthode get_letter

# MySubClass hérite de cette classe, et donc du même attribut et de la même
# méthode. Observez bien les lignes 13 et 15 pour comprendre comment l'héritage
# se met en place.

# En plus des attributs et méthodes hérités, MySubClass possède un attribut
# number et une méthode get_number en supplément.

# Reprenez votre classe User.
# Créez une classe Student qui hérite de User et qui :
# - possède un attribut privé _school (str)
# - possède un attribut privé _level (int)
# - possède une méthode has_degree() qui renvoit True si le level est supérieur
# ou égal à 3

################################################################################
class User :
    def __init__(self, fn, ln, age):
        self._firstname = fn
        self._lastname = ln
        self._age = age
        self._followers = 0
    
    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_age(self):
        return self._age

    def get_followers(self):
        return self._followers

    def _is_adult(self) :
        if (self.get_age() >= 18 ) :
            return True
        else :
            return False
    
    def get_full_name(self) :
        return self.get_firstname() + " " + self.get_lastname()

    def add_followers(self, n):
        if (self._is_adult()) :
            self.followers = self.followers +n

def get_oldest(user1, user2) :
    if (user1.get_age() > user2.get_age()) :
        return user1.get_full_name()
    else :
        return user2.get_full_name()

class Student(User):
    def __init__(self, fn, ln, age, s, l):
        User.__init__(self, fn, ln, age)
        self._school = s
        self._level = l

    def get_school(self):
        return self._school
    
    def get_level(self):
        return self._level

    def has_degree(self) :
        if (self.get_level() >= 3) :
            return True
        else :
            return False

################################################################################

# Pour vérifier que l'héritage est pertinent, demandez-vous si tous les Student
# sont des User et si chaque attribut et méthode s'appliquent aussi à un
# Student. Student est un type d'User particulier, une extension.

# Bien sûr, l'héritage multi-niveau est possible.

















test = Student("bob", "doe", 18, "cnam", 3)
test_bis = Student("bob", "doe", 18, "cnam", 2)
print('\033[92m✓ OK' if test.get_full_name() == "bob doe" and test._school == "cnam" and test._level == 3 and test.has_degree() and not test_bis.has_degree() else '\033[91m❌KO')