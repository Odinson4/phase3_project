import time
import numpy as np
import sys
# import colorama
# Delay printing


def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class


class Battle:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20  # Amount of health bars

    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other
        string_1_attack = ''
        string_2_attack = ''
        total_money = 0

        # Print fight information
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack, Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass', 'Electric',
                   'Psychic', 'Ground', 'Fighting', 'Normal']

        for i, k in enumerate(version):
            if self.types == k:
                # Both are same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is STRONG
                if Pokemon2.types == version[(i+1) % 8] or Pokemon2.types == version[(i+6) % 8]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is WEAK
                if Pokemon2.types == version[(i+2) % 8] or Pokemon2.types == version[(i+5) % 8]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'

        # Now for the actual fighting...
        # Continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break

            # Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")
        total_money += money  # add the money won to the total

        print("Total money accrued:", total_money)


if __name__ == '__main__':
    # Create Pokemon

    available_pokemon = [
        Battle(f"{red}Mewtwo{Style.RESET_ALL}", 'Psychic', [f"{blue}Confusion{Style.RESET_ALL}", f"{blue}Psybeam{Style.RESET_ALL}",
               f"{blue}Ice Beam{Style.RESET_ALL}", f"{green}Mega Punch{Style.RESET_ALL}"], {'ATTACK': 15, 'DEFENSE': 50}),

        Battle(f"{yellow}Pikachu{Style.RESET_ALL}", 'Electric', [f"{blue}Thunderbolt{Style.RESET_ALL}", f"{blue}Thunder Shock{Style.RESET_ALL}",
               f"{cyan}Iron Tail{Style.RESET_ALL}", f"{green}Quick Attack{Style.RESET_ALL}"], {'ATTACK': 5, 'DEFENSE': 3}),

        Battle(f"{magenta}Snorlax{Style.RESET_ALL}", 'Normal', [f"{green}Body Slam{Style.RESET_ALL}", f"{cyan}Rest{Style.RESET_ALL}",
               f"{green}Hyper Beam{Style.RESET_ALL}", f"{yellow}Yawn{Style.RESET_ALL}"], {'ATTACK': 7, 'DEFENSE': 12}),

        Battle(f"{yellow}Jigglypuff{Style.RESET_ALL}", 'Normal', [
               f"{green}Sing{Style.RESET_ALL}", f"{green}Body Slam{Style.RESET_ALL}", f"{cyan}Rest{Style.RESET_ALL}", f"{yellow}Rollout{Style.RESET_ALL}"], {'ATTACK': 2, 'DEFENSE': 2}),

        Battle(f"{blue}Gyarados{Style.RESET_ALL}", 'Water', [f"{green}Waterfall{Style.RESET_ALL}", f"{blue}Dragon Rage{Style.RESET_ALL}",
               f"{green}Bite{Style.RESET_ALL}", f"{green}Hyper Beam{Style.RESET_ALL}"], {'ATTACK': 12, 'DEFENSE': 8}),

        Battle(f"{cyan}Onix{Style.RESET_ALL}", 'Ground', [f"{green}Rock Throw{Style.RESET_ALL}", f"{cyan}Dig{Style.RESET_ALL}",
               f"{cyan}Iron Tail{Style.RESET_ALL}", f"{yellow}Bind{Style.RESET_ALL}"], {'ATTACK': 6, 'DEFENSE': 14}),

        Battle(f"{red}Machamp{Style.RESET_ALL}", 'Fighting', [f"{green}Karate Chop{Style.RESET_ALL}", f"{blue}Cross Chop{Style.RESET_ALL}",
               f"{yellow}Submission{Style.RESET_ALL}", f"{yellow}Seismic Toss{Style.RESET_ALL}"], {'ATTACK': 16, 'DEFENSE': 8}),

        Battle(f"{red}Charizard{Style.RESET_ALL}", 'Fire', [f"{green}Flamethrower{Style.RESET_ALL}", f"{cyan}Fly{Style.RESET_ALL}",
               f"{blue}Blast Burn{Style.RESET_ALL}", f"{green}Fire Punch{Style.RESET_ALL}"], {'ATTACK': 12, 'DEFENSE': 8}),

        Battle(f"{blue}Blastoise{Style.RESET_ALL}", 'Water', [f"{green}Water Gun{Style.RESET_ALL}", f"{green}Bubblebeam{Style.RESET_ALL}",
               f"{blue}Hydro Pump{Style.RESET_ALL}", f"{blue}Surf{Style.RESET_ALL}"], {'ATTACK': 10, 'DEFENSE': 10}),

        Battle('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], {
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
    player_pokemon.fight(opponent_pokemon)
