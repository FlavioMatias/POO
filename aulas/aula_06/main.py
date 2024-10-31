class Entity:
    """Classe base para qualquer entidade do jogo."""
    def __init__(self, life: int, speed: int, sprite: str, rect: tuple):
        self.life = life
        self.speed = speed
        self.sprite = sprite
        self.rect = rect

    def move(self, direction: str):
        """Move uma entidade numa direção específica."""
        print(f"{self.__class__.__name__} movendo para {direction}")

    def __str__(self):
        return f"{self.__class__.__name__} | Vida: {self.life}"


class Monster(Entity):
    """Classe para monstros do jogo."""
    def __init__(self, life: int, atk: int, speed: int, sprite: str, rect: tuple):
        super().__init__(life, speed, sprite, rect)
        self.atk = atk

    def attack(self, target: Entity):
        """Ataca uma entidade alvo."""
        print(f"{self.__class__.__name__} atacando {target.__class__.__name__} com {self.atk} de dano")
        target.life -= self.atk

    def __str__(self):
        return f"Monstro | Vida: {self.life}, Ataque: {self.atk}, Velocidade: {self.speed}"


class NPC(Entity):
    """Classe para personagens não-jogáveis do jogo."""
    def __init__(self, life: int, speed: int, sprite: str, rect: tuple, role: str):
        super().__init__(life, speed, sprite, rect)
        self.role = role

    def eat(self, food: str):
        """Método que permite ao NPC comer algo."""
        print(f"{self.__class__.__name__} comendo {food}")

    def trade(self, currency: str, item: str):
        """Método para comércio com o jogador."""
        print(f"{self.__class__.__name__} trocando {item} por {currency}")

    def talk(self, message: str):
        """Método para fazer o NPC falar."""
        print(f"{self.__class__.__name__}: {message}")

    def __str__(self):
        return f"{self.role} NPC | Vida: {self.life}"


class Player(Entity):
    """Classe para o jogador."""
    def __init__(self, nickname: str):
        super().__init__(life=100, speed=10, sprite="player_sprite", rect=(40, 80))
        self.nickname = nickname
        self.inventory = {}
        self.level = 1
        self.experience = 0
        self.stamina = 50
        self.mana = 30
        self.defense = 5
        self.equipment = {
            "weapon": None,
            "armor": None,
            "accessory": None
        }
        self.skills = []

    def gain_experience(self, amount: int):
        """Ganha experiência e sobe de nível quando necessário."""
        self.experience += amount
        print(f"{self.nickname} ganhou {amount} de experiência!")
        while self.experience >= 100 * self.level:
            self.level_up()

    def level_up(self):
        """Método para subir de nível, aumentando atributos do jogador."""
        self.level += 1
        self.life += 20
        self.stamina += 10
        self.mana += 10
        self.defense += 2
        self.experience = 0
        print(f"{self.nickname} subiu para o nível {self.level}!")

    def add_to_inventory(self, item, quantity=1):
        """Adiciona um item ao inventário do jogador."""
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print(f"{item} adicionado ao inventário de {self.nickname}.")

    def equip(self, item_type: str, item: str):
        """Equipa um item em um dos slots de equipamento."""
        if item_type in self.equipment:
            self.equipment[item_type] = item
            print(f"{item} equipado como {item_type}.")

    def attack(self, target: Entity):
        """Ataca uma entidade alvo, levando em consideração o ataque e a defesa."""
        weapon_damage = 10  # Exemplo de dano fixo; poderia variar conforme a arma equipada
        damage = max(0, weapon_damage + (self.level * 2) - target.defense)
        target.life -= damage
        print(f"{self.nickname} ataca {target.__class__.__name__} causando {damage} de dano!")

    def use_skill(self, skill_name: str, target: Entity = None):
        """Usa uma habilidade desbloqueada, se disponível."""
        if skill_name in self.skills:
            print(f"{self.nickname} usa {skill_name} em {target.__class__.__name__}!" if target else f"{self.nickname} usa {skill_name}!")
        else:
            print(f"{self.nickname} não possui a habilidade {skill_name}.")

    def heal(self, amount: int):
        """Cura o jogador, sem ultrapassar o valor máximo de vida."""
        self.life = min(100 + self.level * 20, self.life + amount)
        print(f"{self.nickname} curou {amount} pontos de vida.")

    def __str__(self):
        return (
            f"Player: {self.nickname} | Nível: {self.level} | Vida: {self.life} | "
            f"Stamina: {self.stamina} | Mana: {self.mana} | Defesa: {self.defense} | Inventário: {self.inventory}"
        )


class Wolf(Monster):
    """Classe para o monstro Lobo."""
    def __init__(self):
        super().__init__(life=100, atk=20, speed=15, sprite="lobo_sprite", rect=(30, 50))

    def __str__(self):
        return f"Lobo | Vida: {self.life}, Ataque: {self.atk}, Velocidade: {self.speed}"


class Goblin(Monster):
    """Classe para o monstro Goblin."""
    def __init__(self):
        super().__init__(life=50, atk=10, speed=20, sprite="goblin_sprite", rect=(20, 40))

    def __str__(self):
        return f"Goblin | Vida: {self.life}, Ataque: {self.atk}, Velocidade: {self.speed}"


class Villager(NPC):
    """Classe para aldeões no jogo."""
    def __init__(self):
        super().__init__(life=100, speed=2, sprite="villager_sprite", rect=(20, 40), role="Aldeão")


class Item:
    """Classe base para itens do jogo."""
    def __init__(self, name: str, item_type: str):
        self.name = name
        self.item_type = item_type

    def __str__(self):
        return f"{self.name} ({self.item_type})"


class Consumable(Item):
    """Classe para itens consumíveis como comida."""
    def __init__(self, name: str, heal_amount: int):
        super().__init__(name, "Consumível")
        self.heal_amount = heal_amount

    def use(self, player: Player):
        """Usa o item consumível, curando o jogador."""
        player.heal(self.heal_amount)
        print(f"{player.nickname} usou {self.name} e curou {self.heal_amount} pontos de vida!")


class Weapon(Item):
    """Classe para armas."""
    def __init__(self, name: str, damage: int):
        super().__init__(name, "Arma")
        self.damage = damage


class CraftingItem(Item):
    """Classe para itens de craft."""
    def __init__(self, name: str):
        super().__init__(name, "Item de Craft")


# Exemplo de uso:
player = Player("Flavio")
print(player)

# Ganhando experiência
player.gain_experience(150)  # Ganhou mais de 100 pontos de experiência

# Adicionando e usando itens
health_potion = Consumable("Poção de Cura", 30)
player.add_to_inventory(health_potion)
health_potion.use(player)

# Criando monstros
wolf = Wolf()
print(wolf)
wolf.attack(player)  # O lobo ataca o jogador
print(player)
