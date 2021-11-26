# Une transformation map ne doit nécessairement conserver le type d'entrée.
# Ainsi, il est tout à fait possible de transformer un tableau d'entiers en un
# tableau de booleen, ou un tableau de dictionnaires en un tableau de strings.

# Grâce à map, transformez cette liste d'utilisateurs en tableau de strings du
# type : ["John Doe is 28", "Jane Doe is 32", ...]. Stockez le résultat dans
# une variable "user_informations".

# Attention : certains utilisateurs n'ont pas d'âge. Dans ce cas, n'ajoutez pas
# la partie "is...".

from typing import TypedDict

class User(TypedDict):
    firstname: str
    lastname: str
    age: int | None

users: list[User] = [
  {
    "firstname": "John",
    "lastname": "Doe",
    "age": 28
  },
  {
    "firstname": "Jane",
    "lastname": "Doe",
    "age": 32
  },
  {
    "firstname": "Allan",
    "lastname": "Doe",
    "age": None
  }
]

################################################################################
def user_stringify(user: User) -> str:
  u=user['firstname'] + " " + user['lastname']
  if (user['age'] != None) :
    u=u + " is " + str(user['age'])
  return u

user_informations: list[str] = list(map(user_stringify, users))
print(user_informations)
################################################################################































print('\033[92m✓ OK' if user_informations == ["John Doe is 28", "Jane Doe is 32", "Allan Doe"] else '\033[91m❌KO')
