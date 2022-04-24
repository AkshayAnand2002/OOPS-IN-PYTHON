###INHERITANCE EXAMPLE-->
class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add nother Cat


class Micheal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)

animal_1 = Simon(name="Simon", age=14)
animal_2 = Sally(name="Sally", age=15)
animal_3 = Micheal(name="Micheal", age=11)

my_cats = [animal_1, animal_2, animal_3]

# 3 Instantiate the Pet class with all your cats use variable my_pets

my_pets = []
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance

my_pets.walk()
########################################################################
#Dunder Method continued--->
class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
action_figure = Toy('red',0)
print(action_figure.__str__())
###the above is exactly same as doing below command.
print(str(action_figure))
##The Dunder method __str__() has the same output as str().
class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
    def __str__(self):
        return f'{self.color}'
action_figure = Toy('red',0)
print(action_figure.__str__())
##We modified dunder method to get different outputs .
##usually dunder methods should not be modified.
class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
    def __str__(self):
        return f'{self.color}'
    def __len__(self):
        return 5
action_figure = Toy('red',0)
print(action_figure.__str__())
print(len(action_figure))
###changed length dunder to return 5.
class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
    def __str__(self):
        return f'{self.color}'
    def __len__(self):
        return 5
    def __del__(self):
        print('deleted!!!')
action_figure = Toy('red',0)
print(action_figure.__str__())
print(len(action_figure))
del action_figure
##changed del dunder
class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
    def __str__(self):
        return f'{self.color}'
    def __len__(self):
        return 5
    def __del__(self):
        print('deleted!!!')
    def __call__(self):
        return('yess??')
action_figure = Toy('red',0)
print(action_figure.__str__())
print(len(action_figure))
#del action_figure
print(action_figure())##special property of call without writing call.
print(action_figure.__call__())###to __call__ i.e. call the function.
###using call we have a special way to call the function.
class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
        self.my_dict={
            'name':'abcd' ,
             'has_pets':False
            }
    def __str__(self):
        return f'{self.color}'
    def __len__(self):
        return 5
    def __del__(self):
        print('deleted!!!')
    def __call__(self):
        return('yess??')
    def __getitem__(self,i):
        return self.my_dict[i]
action_figure = Toy('red',0)
print(action_figure.__str__())
print(len(action_figure))
print(action_figure['name'])##to access name of key
#######################################################################
class SuperList():
    def __len__(self):
        return 1000
super_list1=SuperList()
print(len(super_list1))
#len(super_list1)
super_list1.append(5)
super_list1[5]
##gives error as superlist is inherited from list.
class SuperList(list):
    def __len__(self):
        return 1000
super_list1 = SuperList()
print(len(super_list1))
print(issubclass(SuperList,list))##True
#len(super_list1)
super_list1.append(5)
print(super_list1[0])##prints 5.
#####################################################
class SuperList(list):
    def __len__(self):
        return 1000
my_list = SuperList([1, 2, 3, 4])
my_list.append(5)
print(my_list) # [1, 2, 3, 4, 5]
print(len(my_list)) # 1000
###############################################################
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
        def run(self):
            print('ran really fast')
##class HybridBorg()--- continued program below i.e. next program.
wizard1=Wizard('Merlin',50,'merlin@gmail.com')
archer1=Archer('Robin',30)
print(wizard1.email)
print(wizard1.sign_in())
print(wizard1.attack())
####################################################################################################
class User:
    def sign_in(self):
        print('logged in')

class Wizard(User):##inside bracket user is written to inherit from User class
    def __init__(self,name,power):
        User.__init__(self)
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

    def run(self):
        print('ran really fast')
class HybridBorg(Wizard,Archer):
    pass
hb1 = HybridBorg('Borgie',50)
print(hb1.run())