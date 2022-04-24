#Inheritance allows new objects to take on properties of existing objects
#We can inherit classes.
class User:
    def sign_in(self):
        print('logged in')
class Wizard(User):##inside bracket user is written to inherit from User class
    pass
class Archer(User):
    pass
wizard1=Wizard()
print(wizard1)
print(wizard1.sign_in())
#################################################################
class User:
    def sign_in(self):
        print('logged in')
class Wizard(User):##inside bracket user is written to inherit from User class
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')
class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')

wizard1=Wizard('Merlin',50)
archer1=Archer('Robin',100)
print(wizard1)
print(wizard1.sign_in())
print(archer1.sign_in())
wizard1.attack()
archer1.attack()
##Both have signin function at the same time --due to inheritance.
##Chilren of classes/main classes is called subclasses or derived classes.
##as derived from from the user class.
##python function to check if something is an instance of a class.
##isinstance(instance,class)
class User:
    def sign_in(self):
        print('logged in')
class Wizard(User):##inside bracket user is written to inherit from User class
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')
class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')

wizard1=Wizard('Merlin',50)
archer1=Archer('Robin',30)
print(wizard1)
print(isinstance(wizard1,Wizard))
##output True as wizard1 is an instance of wizard.
print(isinstance(wizard1,User))
##Outputs True as wizard1 is instance of wizard which is instance
#of User.
#Everything in python inherits from the base object class that python comes with
#and is called object.
print(isinstance(wizard1,object))
#methods or functions belong to objects.
#we use self keyword to act upon the object that got instantiated.
#Polymorphism refers to the way in which object classes can share the same
#method name.But those method names can act differently based on what object
#calls them.
print(wizard1.attack())
def player_attack(char):
    char.attack()
player_attack(wizard1)
player_attack(archer1)
##same function gives different output even though we are calling the same thing
#because of the object we pass into it.--->POLYMORPHISM
for char in [wizard1,archer1]:
    char.attack()
##2 different outputs even though calling the same method because of different
## objects.-->Polymorphism
# if a function is in both wizard(derived class)and user (main class) and attack
#in user return nothing but attack in wizard return then we will get output of
# attack in wizard class as it will overwrite that from user.

class User:
    def sign_in(self):
        print('logged in')
    def attack(self):
        print('DO NOTHING')
class Wizard(User):##inside bracket user is written to inherit from User class
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def attack(self):
        User.attack(self)##TO GET ATTACK PRESENT IN THE User CLASS
        print(f'attacking with power of {self.power}')
class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')
wizard1=Wizard('Merlin',50)
archer1=Archer('Robin',30)
#print(wizard1)
print(wizard1.attack())
##PRINTS DO NOTHING AS WELL AS ATTACKING WITH A POWER OF 50.
##BECAUSE USER.ATTACK(SELF) AND NEXT LINE BOTH GET EXECUTED.
#def player_attack(char):
 #   char.attack()
#player_attack(wizard1)
#player_attack(archer1)
##############
# 4 PILLARS OF OOP--ENCAPSULATION,ABSTRACTION,INHERITANCE,POLYMORPHISM

class User:
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print('logged in')
    def attack(self):
        print('DO NOTHING')
class Wizard(User):##inside bracket user is written to inherit from User class
    def __init__(self,name,power,email):
        User.__init__(self,email)
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')
class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')
wizard1=Wizard('Merlin',50,'merlin@gmail.com')
archer1=Archer('Robin',30)
print(wizard1.email)
print(wizard1.sign_in())
print(wizard1.attack())
##in above prog we did same thing we called init method of User inside class
#Wizard.
##Another way of doing above program is by super().
class User:
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print('logged in')
    def attack(self):
        print('DO NOTHING')
class Wizard(User):##inside bracket user is written to inherit from User class
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')
class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')
wizard1=Wizard('Merlin',50,'merlin@gmail.com')
archer1=Archer('Robin',30)
print(wizard1.email)
print(wizard1.sign_in())
print(wizard1.attack())
###super() refers to super clas or class above wizard which is user.
##with super no need of self.
##we get same correct output.
##introspection in computer programming means the ability to determine the type
##of an object at run time.
##dir -> gives all methods and attributes that the instance has .
print(dir(wizard1))
##it shows type of object, class inherited from parent or base object  class etc.
##len of python implemented by dunder method.
##Dunder methods allow us to see python specific functions on objects created
##through our class.
