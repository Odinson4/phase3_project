import sqlite3
from battle import Battle
from pokemon import Pokemon
from trainer import Trainer
from colorama import Fore, Style, Back


class Pokemondb:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def create_tables(self):
        # Create Moves table
        self.c.execute('''CREATE TABLE IF NOT EXISTS Moves (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      pokemon_type TEXT,
                      power INTEGER,
                      accuracy INTEGER
                  )''')

        # Create Moveset table
        self.c.execute('''CREATE TABLE IF NOT EXISTS Moveset (
                      id INTEGER PRIMARY KEY,
                      move1_name TEXT,
                      move2_name TEXT,
                      move3_name TEXT,
                      move4_name TEXT
                  )''')

        # Create Pokemon table
        self.c.execute('''CREATE TABLE IF NOT EXISTS Pokemon (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      pokemon_type TEXT,
                      moveset INTEGER,
                      hp INTEGER,
                      attack INTEGER,
                      defense INTEGER,
                      speed INTEGER,
                      FOREIGN KEY (moveset) REFERENCES Moveset(id)
                  )''')

        # Create Trainers table
        self.c.execute('''CREATE TABLE IF NOT EXISTS Trainers (
                      id INTEGER PRIMARY KEY,
                      name TEXT
                  )''')

        # Create Trainer_Pokemon table
        self.c.execute('''CREATE TABLE IF NOT EXISTS Trainer_Pokemon (
                      id INTEGER PRIMARY KEY,
                      trainer_name TEXT,
                      pokemon_name TEXT,
                      FOREIGN KEY (trainer_name) REFERENCES Trainers(name),
                      FOREIGN KEY (pokemon_name) REFERENCES Pokemon(name)
                  )''')
        self.conn.commit()

    def add_pokemon(self, name, pokemon_type, moveset_id, hp, attack, defense, speed):
        self.c.execute("INSERT INTO Pokemon VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                       (name, pokemon_type, moveset_id, hp, attack, defense, speed))
        self.conn.commit()

    def display_pokemon(self):
        self.c.execute("SELECT * FROM Pokemon")
        rows = self.c.fetchall()
        pokemon_strings = []
        for row in rows:
            poke = Pokemon(*row)
            pokemon_strings.append(str(poke))
        return pokemon_strings

    def delete_pokemon(self, id):
        self.c.execute("DELETE FROM Pokemon WHERE id = ?",
                       (id))
        self.conn.commit()
        return self.c.rowcount

    def update_pokemon(self, pokemon):
        self.c.execute('''UPDATE Pokemon SET name = ?, pokemon_type = ?, moveset = ?, hp = ?, attack = ?, defense = ?, speed = ? WHERE id = ?''',
                       (pokemon.name, pokemon.pokemon_type, pokemon.moveset, pokemon.hp, pokemon.attack, pokemon.defense, pokemon.speed, pokemon.id))
        self.conn.commit()
        return self.c.rowcount

    def add_trainer(self, trainer_name):
        # Check if the trainer name already exists
        self.c.execute(
            '''SELECT name FROM Trainers WHERE name=?''', (trainer_name,))
        result = self.c.fetchone()
        if result:
            print(f"Trainer with name '{trainer_name}' already exists")
            return

        # Insert a new record if the trainer name does not exist
        self.c.execute(
            '''INSERT INTO Trainers(name) VALUES (?)''', (trainer_name,))
        self.conn.commit()


db = Pokemondb("./pokemon.db")
db.create_tables()
# colorama.init(autoreset=True)

print(Fore.RED + '''

██████╗░░█████╗░██╗░░██╗███████╗███╗░░░███╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░████║██╔══██╗████╗░██║
██████╔╝██║░░██║█████═╝░█████╗░░██╔████╔██║██║░░██║██╔██╗██║
██╔═══╝░██║░░██║██╔═██╗░██╔══╝░░██║╚██╔╝██║██║░░██║██║╚████║
██║░░░░░╚█████╔╝██║░╚██╗███████╗██║░╚═╝░██║╚█████╔╝██║░╚███║
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝

''' + Style.RESET_ALL)

trainer_name = input("Enter your name: ")

# Create a Trainer object and add it to the Trainers table
trainer = Trainer(trainer_name)
db.add_trainer(trainer.name)


while True:
    print("\nPlease choose an option:\n")
    print(Fore.GREEN + "1. " + Style.BRIGHT + "Add a new Pokemon")
    print(Fore.BLUE + "2. " + Style.BRIGHT + "Delete an existing Pokemon")
    print(Fore.YELLOW + "3. " + Style.BRIGHT + "Display All Pokemon")
    print(Fore.CYAN + "4. " + Style.BRIGHT + "Update a Pokemon")
    print(Fore.MAGENTA + "5. " + Style.BRIGHT + "Battle a Random Pokemon")
    print(Fore.RED + "6. " + Style.BRIGHT + "Quit" + Style.RESET_ALL)

    choice = input("Choose an option: ")

    if choice == '1':
        name = input("\nEnter Pokemon Name: \n")
        pokemon_type = input("\nEnter Pokemon Type: \n")
        moveset_id = input("\nEnter Pokemon Moveset: \n")
        hp = input("\nEnter Pokemon HP: \n")
        attack = input("\nEnter Pokemon Attack: \n")
        defense = input("\nEnter Pokemon Defense: \n")
        speed = input("\nEnter Pokemon Speed: \n")
        db.add_pokemon(name, pokemon_type, moveset_id,
                       hp, attack, defense, speed)
        print(f"\n{name} is now a Pokemon!\n")

    elif choice == '2':
        id = input("\nEnter Pokemon ID: \n")
        deleted = db.delete_pokemon(id)
        if deleted:
            print("\nYour Pokemon has been deleted\n")
        else:
            print("\nMaybe not...\n")
        pass

    elif choice == '3':
        pokemon = db.display_pokemon()
        if pokemon:
            for poke in pokemon:
                print(pokemon)

    elif choice == '4':
        id = input("\nEnter Pokemon ID: \n")
        name = input("\nEnter Pokemon Name: \n")
        pokemon_type = input("\nEnter Pokemon Type: \n")
        moveset_id = input("\nEnter Pokemon Moveset: \n")
        hp = input("\nEnter Pokemon HP: \n")
        attack = input("\nEnter Pokemon Attack: \n")
        defense = input("\nEnter Pokemon Defense: \n")
        speed = input("\nEnter Pokemon Speed: \n")
        pokemon = Pokemon(id, name, pokemon_type, moveset_id,
                          hp, attack, defense, speed)

        updated = db.update_pokemon(pokemon)

        if updated:
            print("\nYour pokemon has been updated\n")
        else:
            print("\nKeep it classy San Diego\n")

    elif choice == '5':
        red = Fore.RED
        green = Fore.GREEN
        blue = Fore.BLUE
        yellow = Fore.YELLOW
        magenta = Fore.MAGENTA
        cyan = Fore.CYAN
        grey = Fore.LIGHTWHITE_EX

        available_pokemon = [
            Battle(f"{magenta}Mewtwo{Style.RESET_ALL}", f"{magenta}Psychic{Style.RESET_ALL}", [f"{magenta}Confusion{Style.RESET_ALL}", f"{magenta}Psybeam{Style.RESET_ALL}",
                                                                                               f"{magenta}Ice Beam{Style.RESET_ALL}", f"{cyan}Mega Punch{Style.RESET_ALL}"], {'ATTACK': 15, 'DEFENSE': 50}),

            Battle(f"{yellow}Pikachu{Style.RESET_ALL}", f"{yellow}Electric{Style.RESET_ALL}", [f"{yellow}Thunderbolt{Style.RESET_ALL}", f"{yellow}Thunder Shock{Style.RESET_ALL}",
                                                                                               f"{cyan}Iron Tail{Style.RESET_ALL}", f"{cyan}Quick Attack{Style.RESET_ALL}"], {'ATTACK': 5, 'DEFENSE': 3}),

            Battle(f"{cyan}Snorlax{Style.RESET_ALL}", 'Normal', [f"{cyan}Body Slam{Style.RESET_ALL}", f"{cyan}Rest{Style.RESET_ALL}",
                                                                 f"{cyan}Hyper Beam{Style.RESET_ALL}", f"{cyan}Yawn{Style.RESET_ALL}"], {'ATTACK': 7, 'DEFENSE': 12}),

            Battle(f"{cyan}Jigglypuff{Style.RESET_ALL}", 'Normal', [
                f"{cyan}Sing{Style.RESET_ALL}", f"{cyan}Body Slam{Style.RESET_ALL}", f"{cyan}Rest{Style.RESET_ALL}", f"{cyan}Rollout{Style.RESET_ALL}"], {'ATTACK': 2, 'DEFENSE': 2}),

            Battle(f"{blue}Gyarados{Style.RESET_ALL}", 'Water', [f"{blue}Waterfall{Style.RESET_ALL}", f"{blue}Dragon Rage{Style.RESET_ALL}",
                                                                 f"{cyan}Bite{Style.RESET_ALL}", f"{cyan}Hyper Beam{Style.RESET_ALL}"], {'ATTACK': 12, 'DEFENSE': 8}),

            Battle(f"{cyan}Onix{Style.RESET_ALL}", 'Ground', [f"{cyan}Rock Throw{Style.RESET_ALL}", f"{cyan}Dig{Style.RESET_ALL}",
                                                              f"{cyan}Iron Tail{Style.RESET_ALL}", f"{cyan}Bind{Style.RESET_ALL}"], {'ATTACK': 6, 'DEFENSE': 14}),

            Battle(f"{cyan}Machamp{Style.RESET_ALL}", 'Fighting', [f"{cyan}Karate Chop{Style.RESET_ALL}", f"{cyan}Cross Chop{Style.RESET_ALL}",
                                                                   f"{cyan}Submission{Style.RESET_ALL}", f"{cyan}Seismic Toss{Style.RESET_ALL}"], {'ATTACK': 16, 'DEFENSE': 8}),

            Battle(f"{red}Charizard{Style.RESET_ALL}", 'Fire', [f"{red}Flamethrower{Style.RESET_ALL}", f"{cyan}Fly{Style.RESET_ALL}",
                                                                f"{red}Blast Burn{Style.RESET_ALL}", f"{red}Fire Punch{Style.RESET_ALL}"], {'ATTACK': 12, 'DEFENSE': 8}),

            Battle(f"{blue}Blastoise{Style.RESET_ALL}", 'Water', [f"{blue}Water Gun{Style.RESET_ALL}", f"{blue}Bubblebeam{Style.RESET_ALL}",
                                                                  f"{blue}Hydro Pump{Style.RESET_ALL}", f"{blue}Surf{Style.RESET_ALL}"], {'ATTACK': 10, 'DEFENSE': 10}),

            Battle(f"{green}Venusaur{Style.RESET_ALL}", 'Grass', [f"{green}Razor Leaf{Style.RESET_ALL}", f"{green}Solarbeam{Style.RESET_ALL}",
                                                                  f"{green}Leech Seed{Style.RESET_ALL}", f"{green}Vine Whip{Style.RESET_ALL}"], {
                'ATTACK': 8, 'DEFENSE': 12})

        ]
        print("Choose your Pokemon:")
        for i, pokemon in enumerate(available_pokemon):
            print(f"{i+1}. {pokemon.name}")
        player_pokemon_index = int(input()) - 1
        player_pokemon = available_pokemon[player_pokemon_index]

        # Prompt the user to select the opponent's Pokemon
        print("Choose your opponent's Pokemon:")
        for i, pokemon in enumerate(available_pokemon):
            if i != player_pokemon_index:
                print(f"{i+1}. {pokemon.name}")
        opponent_pokemon_index = int(input()) - 1
        opponent_pokemon = available_pokemon[opponent_pokemon_index]

        # Start the battle
#         print('''


# ██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗
# ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝
# ██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░
# ██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░
# ██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗
# ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝


#         ''')
        player_pokemon.fight(opponent_pokemon)

    elif choice == '6':
        print('''
              
        
░█████╗░░█████╗░████████╗░█████╗░██╗░░██╗  ██╗░░░██╗░█████╗░  ██╗░░░░░░█████╗░████████╗███████╗██████╗░░░░
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░██║  ╚██╗░██╔╝██╔══██╗  ██║░░░░░██╔══██╗╚══██╔══╝██╔════╝██╔══██╗░░░
██║░░╚═╝███████║░░░██║░░░██║░░╚═╝███████║  ░╚████╔╝░███████║  ██║░░░░░███████║░░░██║░░░█████╗░░██████╔╝░░░
██║░░██╗██╔══██║░░░██║░░░██║░░██╗██╔══██║  ░░╚██╔╝░░██╔══██║  ██║░░░░░██╔══██║░░░██║░░░██╔══╝░░██╔══██╗██╗
╚█████╔╝██║░░██║░░░██║░░░╚█████╔╝██║░░██║  ░░░██║░░░██║░░██║  ███████╗██║░░██║░░░██║░░░███████╗██║░░██║╚█║
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚╝

███╗░░██╗███████╗██████╗░██████╗░░░░░░░
████╗░██║██╔════╝██╔══██╗██╔══██╗░░░░░░
██╔██╗██║█████╗░░██████╔╝██║░░██║░░░░░░

██║╚████║██╔══╝░░██╔══██╗██║░░██║░░░░░░
██║░╚███║███████╗██║░░██║██████╔╝██╗██╗
╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═╝
              ''')
        break

    else:
        print("\nInvalid Choice. Please try again.\n")
