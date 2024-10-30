class Monster:
    def __init__(self, life, atk, speed, sprite, rect):
        self.life = life
        self.atk = atk
        self.speed = speed
        self.sprite = sprite
        self.rect = rect
    def move(self):
        print("andou")
    def atack(self):
        print("atacando")
        
    
class Lobo(Monster):
    def __init__(self):
        super().__init__(life=100, atk=20, speed=15, sprite="lobo_sprite", rect=(30, 50))

class Goblin(Monster):
    def __init__(self):
        super().__init__(life=50, atk=10, speed=20, sprite="goblin_sprite", rect=(20, 40))

# Exemplo de instâncias
lobo = Lobo()
print(f"Lobo -> Vida: {lobo.life}, Ataque: {lobo.atk}, Velocidade: {lobo.speed}")
