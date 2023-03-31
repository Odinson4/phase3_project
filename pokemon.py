class Pokemon:

    def __init__(self, id, name, pokemon_type, moveset, hp, attack, defense, speed):
        self.id = id
        self.name = name
        self.pokemon_type = pokemon_type
        self.moveset = moveset
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Type: {self.pokemon_type}, Moveset: {self.moveset}, HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}"
