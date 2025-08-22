import random
import time, sys

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def typingPrint(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.10)

def typingPrint2(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.20)

def typingbackspace(text):
    for character in text:
        sys.stdout.write(character)  # Print the text
        sys.stdout.flush()      # Ensure it's displayed immediately
        time.sleep(0.20)           # Pause for a moment
    
    time.sleep(1)
    for character in text:
        sys.stdout.write('\b' + ' ' + '\b')  # backspace, overwrite with space, backspace again
        sys.stdout.flush()
        time.sleep(0.1)

def typingInput(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
   value = input()  
   return value

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.defense = 5
        self.level = 1
        self.exp = 0
        self.gold = 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 20:  # simple level up rule
            self.level += 1
            self.exp = 0
            self.max_hp += 20
            self.hp = self.max_hp
            self.attack += 5
            self.defense += 2
            print(f"{GREEN}{self.name} leveled up to {self.level}!{RESET}")

    def gain_gold(self, amount):
        self.gold += amount
        print(f"{YELLOW}{self.name} has gained {amount} gold!{RESET}")

    def rest_inn(self, amount):
        while True:
            amount = (30*(self.level*0.5))
            if self.gold > amount:
                response = input(f"\nDo you want to rest at Pandora's Inn for {amount} gold? Y/N?\n > ").lower()
                
                if response == "y":
                    print("Thank you for resting at Pandora's Inn!\n Recovering HP.....")
                    self.gold -= amount 
                    self.hp = self.max_hp
                    break 
                    
                elif response == "n":
                    print("")
                    print("Tsk... Why even bother? Goodbye...")
                    break
                        
                else:
                    print("\nPlease only choose between Yes or No Adventurer!")
                    continue
            
            else:
                typingPrint("\nGO AWAY! WE DON'T WELCOME BEGGARS!")
                time.sleep(1)
                typingbackspace("\n.................")
                time.sleep(1)
                typingPrint("Maybe I should get gold first.....\n")
                time.sleep(2)
                break

    def show_status(self):
        print(f"{self.name} | HP: {RED}{self.hp}/{self.max_hp}{RESET} | ATK: {self.attack} | DEF: {self.defense} | LVL: {self.level} | GOLD: {self.gold}")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0



class Enemy:
    def __init__(self, name, base_hp, base_attack, base_defense, base_exp_reward, player_level, gold_reward):
        self.name = name
        # Scale stats based on player level
        level_multiplier = 1 + (player_level - 1) * 0.3  # 30% increase per level
        self.hp = int(base_hp * level_multiplier)
        self.max_hp = self.hp
        self.attack = int(base_attack * level_multiplier)
        self.defense = int(base_defense * level_multiplier)
        self.exp_reward = int(base_exp_reward * level_multiplier)
        self.gold_reward = gold_reward

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def show_status(self):
        print(f"{self.name} | HP: {RED}{self.hp}/{self.max_hp}{RESET} | ATK: {self.attack} | DEF: {self.defense}")



def adventure(player):
    encounter = random.choices(
        ["Goblin", "Orc", "Kobold", "Slime", "Troll", "None"], 
        weights=[25, 15, 20, 30, 5, 5],  # percentages
        k=1
    )[0]

    if encounter == "Goblin":
        enemy_data = enemy_types[0]
        enemy = Enemy(enemy_data[0], enemy_data[1], enemy_data[2],
                      enemy_data[3], enemy_data[4], player.level, enemy_data[5])
        battle(player, enemy)

    elif encounter == "Orc":
        enemy_data = enemy_types[1]
        enemy = Enemy(enemy_data[0], enemy_data[1], enemy_data[2],
                      enemy_data[3], enemy_data[4], player.level, enemy_data[5])
        battle(player, enemy)

    elif encounter == "Kobold":
        enemy_data = enemy_types[2]
        enemy = Enemy(enemy_data[0], enemy_data[1], enemy_data[2],
                      enemy_data[3], enemy_data[4], player.level, enemy_data[5])
        battle(player, enemy)

    elif encounter == "Slime":
        enemy_data = enemy_types[3]
        enemy = Enemy(enemy_data[0], enemy_data[1], enemy_data[2],
                      enemy_data[3], enemy_data[4], player.level, enemy_data[5])
        battle(player, enemy)

    elif encounter == "Troll":
        enemy_data = enemy_types[4]
        enemy = Enemy(enemy_data[0], enemy_data[1], enemy_data[2],
                      enemy_data[3], enemy_data[4], player.level, enemy_data[5])
        battle(player, enemy)

    else:
        print("\nThe area is peaceful... no enemies this time.")

def random_enemy(player):
    enemy_data = random.choice(enemy_types)  # pick a random enemy
    return Enemy(enemy_data[0], enemy_data[1], enemy_data[2], enemy_data[3], enemy_data[4], player.level, enemy_data[5])

def battle(player, enemy):
    print(f"\n{YELLOW}A wild {enemy.name} appears!{RESET}")
    
    while player.is_alive() and enemy.is_alive():
        print("\n--- Battle ---")
        player.show_status()
        enemy.show_status()

        print("\nChoose an action:")
        print("\n[1] Attack")
        print("[2] Defend")
        print("[3] Run Away")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            # New damage formula considering defense more significantly
            damage = max(1, int(player.attack * (100 / (100 + enemy.defense))))  # Defense reduces damage exponentially
            enemy.take_damage(damage)

            print(f"\n{player.name} attacks {enemy.name} for {damage} damage!")

        elif choice == "2":
            print(f"\n{player.name} defends and reduces damage this turn.")

        elif choice == "3":
            damage = int(player.max_hp * 0.5) 
            player.take_damage(damage)
            print(f"\n{player.name} runs away and loses 50% of his health!")
            return

        else:
            print("\nInvalid choice, you lose your turn!")

        if enemy.is_alive():
            # New enemy damage formula
            damage = max(1, int(enemy.attack * (100 / (100 + player.defense))))
            if choice == "2":
                damage //= 2  # defending still halves the damage
            player.take_damage(damage)
            print(f"{enemy.name} attacks {player.name} for {damage} damage!")

    # End of battle
    if player.is_alive():
        print(f"\n{GREEN}{player.name} defeated {enemy.name}!{RESET}")
        player.gain_exp(enemy.exp_reward)
        player.gain_gold(enemy.gold_reward)

    else:
        print(f"\n{RED}{player.name} has been defeated...{RESET}")
    
player = Player("Hero")
enemy_types = [("Goblin", 30, 8, 3, 10, 15),
         ("Orc", 100, 15, 5, 25, 20 ),
         ("Kobold", 25, 12, 2, 8, 10),
         ("Slime", 15, 5, 1, 5, 5),
         ("Troll", 150, 20, 8, 50, 40)]

while True:
    print("")
    print(f"Welcome to Wilderlands Adventure {player.name}!\n")
    print("---------- STATS ----------")
    print(f"{player.name} | HP: {RED}{player.hp}/{player.max_hp}{RESET}"
          f"| ATK: {player.attack}\n DEF: {player.defense} "
          f"| LVL: {player.level} | GOLD: {player.gold}")
    print("\n[1] Adventure!")
    print("[2] Buy at a Shop!")
    print("[3] Rest at an Inn!")
    print("[4] End Adventure!")
    print("")

    try:
        choice = int(input("Please choose a move from 1-4: "))

        match choice:
            case 1:
                if player.is_alive():
                    adventure(player)

                if not player.is_alive():
                    print("You are dead! Ending adventure...")
                    print("")
                    exit()

            case 2:
                pass
            
            case 3:
                player.rest_inn(player)

            case 4:
                print("")
                typingPrint("Ending adventure.....") 
                time.sleep(1)
                typingPrint2("\nThank you for playing!")
                time.sleep(1)
                print("")
                exit()

    except ValueError:
            print("Please choose from 1-4 only.")
            print("")

    