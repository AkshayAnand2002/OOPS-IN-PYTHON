class PlayerCharacter:
    membership= True #class object attribute i.e. true for all objects made and to be made
    def __init__(self,name,age): ##constructor or init method
        if(self.membership): #we can also write if(PlayerCharacter.membership)
            self.name = name #attributes
            self.age = age#attributes
    def shout(self):
        print(f'my name is {self.name}.')
        #return 'done'
    @classmethod
    def adding_things(cls,num1,num2):#cls means class
        ##we can use classmethod without instantiating a class.
        return num1+num2
player1=PlayerCharacter('Akshay',19)
player2=PlayerCharacter('Abc',20)
player2.attack=50
#print(player1.shout())
#print(player1.shout())
print(player1.adding_things(2,3))
##we can use classmethod without instantiating a class.
##we can use classmethod without instantiating a class.
class PlayerCharacter:
    membership= True #class object attribute i.e. true for all objects made and to be made
    def __init__(self,name,age): ##constructor or init method
        if(self.membership): #we can also write if(PlayerCharacter.membership)
            self.name = name #attributes
            self.age = age#attributes
    def shout(self):
        print(f'my name is {self.name}.')
        #return 'done'
    @classmethod
    def adding_things(cls,num1,num2):#cls means class
        ##we can use classmethod without instantiating a class.
        return num1+num2
#player1=PlayerCharacter('Akshay',19)
#player2=PlayerCharacter('Abc',20)
#player2.attack=50
#print(player1.shout())
#print(player1.shout())
print(PlayerCharacter.adding_things(2,3))
class PlayerCharacter:
    membership= True #class object attribute i.e. true for all objects made and to be made
    def __init__(self,name,age): ##constructor or init method
        if(self.membership): #we can also write if(PlayerCharacter.membership)
            self.name = name #attributes
            self.age = age#attributes
    def shout(self):
        print(f'my name is {self.name}.')
        #return 'done'
    @classmethod
    def adding_things(cls,num1,num2):#cls means class
        ##we can use classmethod without instantiating a class.
        return cls('TEDDY',num1+num2)
#player1=PlayerCharacter('Akshay',19)
#player2=PlayerCharacter('Abc',20)
#player2.attack=50
#print(player1.shout())
#print(player1.shout())
#print(player1.adding_things(2,3))
player3 = PlayerCharacter.adding_things(2,3)
print(player3.age)
# Above created a new player by classmethod.
# In staticmethod we don't have access to cls.
class PlayerCharacter:
    membership= True #class object attribute i.e. true for all objects made and to be made
    def __init__(self,name,age): ##constructor or init method
        if(self.membership): #we can also write if(PlayerCharacter.membership)
            self.name = name #attributes
            self.age = age#attributes
    def shout(self):
        print(f'my name is {self.name}.')
        #return 'done'
    #@classmethod
    #def adding_things(cls,num1,num2):#cls means class
        ##we can use classmethod without instantiating a class.
        #return num1+num2
    @staticmethod
    def adding_things(num1,num2):#cls means class
        return num1+num2
player1=PlayerCharacter('Akshay',19)
player2=PlayerCharacter('Abc',20)
player2.attack=50
#print(player1.shout())
#print(player1.shout())
print(player1.adding_things(2,3))
#Encapsulation is the binding of data and functions that manipulate that
#data and we encapsulate into one big object so that we can keep
#everything in this box that users or code or other machines can interact.
class PlayerCharacter:
    membership= True #class object attribute i.e. true for all objects made and to be made
    def __init__(self,name,age): ##constructor or init method
        if(self.membership): #we can also write if(PlayerCharacter.membership)
            self.name = name #attributes
            self.age = age#attributes
    def shout(self):
        print(f'my name is {self.name}.')
        return 'done'
    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old.')
player1=PlayerCharacter('Akshay',19)
player2=PlayerCharacter('Abc',20)
player2.attack=50
player1.speak()
#print(player1.shout())
#print(player1.shout())
#Through encapsulation we can create multiple objects using class.
#Abstraction means hiding of information or abstracting away information
#and giving access to only what is necessary.
#Only particular user, machine etc is given access.
player1.name = '!!!'
player1.speak = 'BOOOOO'
print(player1.speak)
print(player1.name)
##Any one can change the name and other things and damage the work.
# we need to give only req. access.
class PlayerCharacter:
    membership= True #class object attribute i.e. true for all objects made and to be made
    def __init__(self,name,age): ##constructor or init method
        if(self.membership): #we can also write if(PlayerCharacter.membership)
            self._name = name #attributes
            self._age = age#attributes
    def shout(self):
        print(f'my name is {self._name}.')
        return 'done'
    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old.')
player1=PlayerCharacter('Akshay',19)
player2=PlayerCharacter('Abc',20)
player2.attack=50
player1.speak()
##In python there are 2 private variables. If we put underscore before
#any variable name eg.- _name means it should not be modified.
#__init__ double underscore because of dunder method.
