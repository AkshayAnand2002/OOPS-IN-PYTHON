class PlayerCharacter:
    membership= True #class object attribute i.e. true for all objects made and to be made
    def __init__(self,name,age): ##constructor or init method
        self.name = name #attributes
        self.age = age#attributes
    def run(self):
        print('run')
        #return 'done'
player1=PlayerCharacter('Akshay',19)
player2=PlayerCharacter('Abc',20)
player2.attack=50
print(player1)
print(player1)
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run())
print(player2.run())
print(player2.attack)
print(player2.membership)
print(player1.membership)
class PlayerCharacter:
    membership= True #class object attribute i.e. true for all objects made and to be made
    def __init__(self,name,age): ##constructor or init method
        if(self.membership): #we can also write if(PlayerCharacter.membership)
            self.name = name #attributes
            self.age = age#attributes
    def run(self):
        print('run')
        #return 'done'
player1=PlayerCharacter('Akshay',19)
player2=PlayerCharacter('Abc',20)
player2.attack=50
print(player1)
print(player1)
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run())
print(player2.run())
print(player2.attack)
print(player2.membership)
print(player1.membership)
class PlayerCharacter:
    membership= True #class object attribute i.e. true for all objects made and to be made
    def __init__(self,name,age): ##constructor or init method
        if(self.membership): #we can also write if(PlayerCharacter.membership)
            self.name = name #attributes
            self.age = age#attributes
    def shout(self):
        print(f'my name is {self.name}.')
        return 'done'
player1=PlayerCharacter('Akshay',19)
player2=PlayerCharacter('Abc',20)
player2.attack=50
print(player1.shout())
print(player1.shout())
