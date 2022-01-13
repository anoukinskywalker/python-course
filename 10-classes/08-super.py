# La surcharge de méthodes devient réellement intéressante lorsque l'on s'en
# sert avec le mot clé "super". Ce dernier permet d'appeler des méthodes de la
# classe parente.

# Il devient donc possible de surcharger le fonctionnement d'une méthode tout en
# appelant la méthode originale.

# Voici un exemple :

class MyClass:
    def __init__(self, letter: str):
        self.letter = letter

class MySubClass(MyClass):
    def __init__(self, letter: str, number: int):
        super().__init__(letter)
        self.number = number

# Pour initialiser la classe enfant, nous sommes passé de :
# MyClass.__init__(self, letter)
# à
# super().__init__(letter)

# L'écriture est plus simple et seuls les paramètres varieront d'une classe
# à l'autre.

# Mais il est possible d'utiliser super() dans d'autres méthodes que __init__.

# Reprenez vos classes User et Student
# Actuellement, la méthode add_followers de Student fait quasiment la même chose
# que celle de User, elle vérifie simplement en plus si l'étudiant est diplômé.

# D'une part, cela est redondant, mais si la méthode de User change, la
# cohérence ne sera plus assurée.

# En utilisant super(), modifiez la méthode add_followers pour déléguer toute
# la logique redondante à la classe parente.

# Utilisez également la syntaxe présentée plus haut pour la fonction __init__.

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
            self._followers = self._followers +n

def get_oldest(user1, user2) :
    if (user1.get_age() > user2.get_age()) :
        return user1.get_full_name()
    else :
        return user2.get_full_name()

class Student(User):
    def __init__(self, fn, ln, age, s, l):
        super().__init__(fn, ln, age)
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
    
    def add_followers(self, n):
        if (self._is_adult() and self.has_degree()) :
            self._followers = self._followers +n
################################################################################























user = User("bob", "doe", 18)
user.add_followers(3)
student_with_degree = Student("bob", "doe", 18, "cnam", 3)
student_with_degree.add_followers(1);
student_with_degree.add_followers(2);
student__without_degree = Student("bob", "doe", 18, "cmam", 2)
student__without_degree.add_followers(1);
student__without_degree.add_followers(2);
print('\033[92m✓ OK' if user._followers == 3 and student_with_degree._followers == 3 and student__without_degree._followers == 0 else '\033[91m❌KO')
