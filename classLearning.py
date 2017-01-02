class Character(object):
    def __init__(self, name):
        self.name = name
    def printName(self):
        print self.name

class npclass(Character):
    def __init__(self, name, friendlyName, enemyName):
        super(npclass, self).__init__(name)
        self.friendly = Friendly(friendlyName)
        self.enemy = Enemy(enemyName)

class pclass(Character):
    def __init__(self, name, archerName, GLName, butcherName, weaponName):
        super(pclass, self).__init__(name)
        self.archer = Archer(archerName)
        self.greenLantern = GreenLantern(GLName)
        self.butcher = Butcher(butcherName)
        self.weapon = Weapon(weaponName)

class Friendly:
    def __init__(self, friendlyName):
        self.name = friendlyName

class Enemy:
    def __init__(self, enemyName):
        self.name = enemyName
        self.attackDamage = 5

class Archer:
    def __init__(self, archerName):
        self.name = archerName

class GreenLantern:
    def __init__(self, GLName):
        self.name = GLName

class Butcher:
    def __init__(self, butcherName):
        self.name = butcherName

class Weapon:
    def __init__(self, weaponName):
        self.name = weaponName

np = npclass("Bob", "friendCitizen", "spy")
np.printName()
print np.friendly.name
print np.enemy.name

p = pclass ("George", "Deepika", "RyanGL", "ButcherKali", "Gun")
p.printName()
print p.archer.name
print p.greenLantern.name
print p.butcher.name
print p.weapon.name
