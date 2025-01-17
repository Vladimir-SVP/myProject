import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed, _cords = [0, 0, 0]):
        self.speed = speed
        self._cords = _cords
    def move(self, dx, dy, dz):
        if dz <= 0:
            self._cords = [dx, dy, dz]
            return print("It's too deep, i can't dive :(")
        else:
            self._cords = [dx*self.speed, dy*self.speed, dz*self.speed]
            return self._cords
    def get_cords(self):
        print(f'X:{self._cords[0]} Y:{self._cords[1]} Z:{self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print(f"{self.sound}")
class Bird(Animal):
    beak = True
    def lay_eggs(self):
        x = random.randint(1, 4)
        print("Here are(is)", x, "eggs for you")
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        dz = abs(dz) / 2
        self._cords = [self._cords[0], self._cords[1], dz]
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()