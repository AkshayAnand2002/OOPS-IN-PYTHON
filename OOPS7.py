###MULTIPLE INHERITANCE-----####
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
#################################################################################################################
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
    def check_arrows(self):
        print(f'{self.num_arrows} remaining')
    def run(self):
        print('ran really fast')
class HybridBorg(Wizard,Archer):
    def __init__(self,name,power,num_arrows):
        Archer.__init__(self,name,num_arrows)
        Wizard.__init__(self,name,power)
hb1 = HybridBorg('Borgie',50,100)
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())