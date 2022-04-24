class PlayerCharacter:
    def __init__(self,name): ##constructor or init method
        self.name = name#attributes
    def run(self):
        print('run')
player1=PlayerCharacter('Akshay')
player2=PlayerCharacter('Abc')
print(player1)
print(player1)
print(player1.name)
print(player2.name)
##self reers to those objects not instantiated and will later be initiated.
##self is for player1 and player2.
class PlayerCharacter:
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
##We get None in output as run function does not return anything.
##only prints run.
# we don't get none when we assign return <something>. 
help(list)#to get blueprint of data.
