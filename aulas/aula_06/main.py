class Monster:
    def __init__(self, life, atk, speed, sprite, rect):
        self.life = life
        self.atk = atk
        self.speed = speed
        self.sprite = sprite
        self.rect = rect

    def __str__(self):
        return "a monster"
    def move(self):
        print("andou")
    def atack(self):
        print("atacando")
        
class NPC:
    def __init__(self, life, speed, sprite, rect):
        self.life = life
        self.speed = speed
        self.sprite = sprite
        self.rect = rect
        self.clt = "ajudante de pedreiro"

    def comer():
        pass

    def troca(self, moeda):
        pass
    
    def talking():
        pass
    
    def move():
        pass
        
    
class Wolf(Monster):
    def __init__(self):
        super().__init__(life=100, atk=20, speed=15, sprite="lobo_sprite", rect=(30, 50))

    def __str__(self): 
        return f"({super().__str__()})wolf : {self.life}"

class Goblin(Monster):
    def __init__(self):
        super().__init__(life=50, atk=10, speed=20, sprite="goblin_sprite", rect=(20, 40))
        
    def __str__(self): 
        return f"goblin : {self.life}"


class Vilage(NPC):
    def __init__(self):
        super().__init__(life= 100, speed= 2, sprite= ("lalalla"), rect = (20, 40))



lobo = Wolf()
print(lobo)