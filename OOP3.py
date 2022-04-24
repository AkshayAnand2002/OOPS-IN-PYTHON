##Create a cat class and find oldest cat.
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
#1 Instantiate the Cat object with 3 cats
cat1 = Cat('a', 2)
cat2 = Cat('b', 1)
cat3 = Cat('c', 4)
#2 Create a function that finds the oldest cat
def find_oldest(c1, c2, c3):
    cat_list = [c1.age, c2.age, c3.age]
    return max(cat_list)
#3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {find_oldest(cat1, cat2, cat3)} years old.")
class Cat:
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age
Cat1 = Cat("win",10)
Cat2 = Cat("bright",5)
Cat3 = Cat("Sky", 3)
Cat_age =[Cat1.age,Cat2.age,Cat3.age]
def oldest():
    x = max(Cat_age)
    return x
x = oldest()
print(f'The Cat is {x} years old.')
#Given the below class:
class Cat:
  species = 'mammal'
  def __init__(self, name, age):
    self.name = name
    self.age = age
# 1 Instantiate the Cat objetct with 3 cats
cat1 = Cat('Saul', 1)
cat2 = Cat('Michel', 2)
cat3 = Cat('Seda', 1)
# 2 Find the oldest Cat
def get_oldest_cat(*args):
  return max(args)
# Output
print(f'The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
