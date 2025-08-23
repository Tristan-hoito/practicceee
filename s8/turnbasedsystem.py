# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.defense = 5
        self.level = 1
        self.exp = 0

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

    def show_status(self):
        print(f"{self.name} | HP: {RED}{self.hp}/{self.max_hp}{RESET} | ATK: {self.attack} | DEF: {self.defense} | LVL: {self.level}")

class Enemy:
    def __init__(self, name, base_hp, base_attack, base_defense, base_exp_reward, player_level):
        self.name = name
        # Scale stats based on player level
        level_multiplier = 1 + (player_level - 1) * 0.3  # 30% increase per level
        self.hp = int(base_hp * level_multiplier)
        self.max_hp = self.hp
        self.attack = int(base_attack * level_multiplier)
        self.defense = int(base_defense * level_multiplier)
        self.exp_reward = int(base_exp_reward * level_multiplier)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def show_status(self):
        print(f"{self.name} | HP: {RED}{self.hp}/{self.max_hp}{RESET} | ATK: {self.attack} | DEF: {self.defense}")

def battle(player, enemy):
    print(f"\n{YELLOW}A wild {enemy.name} appears!{RESET}")
    
    while player.is_alive() and enemy.is_alive():
        print("\n--- Battle ---")
        player.show_status()
        enemy.show_status()

        print("\nChoose an action:")
        print("1. Attack")
        print("2. Defend")
        choice = input("Enter your choice: ")

        if choice == "1":
            # New damage formula considering defense more significantly
            damage = max(1, int(player.attack * (100 / (100 + enemy.defense))))  # Defense reduces damage exponentially
            enemy.take_damage(damage)
            print(f"{player.name} attacks {enemy.name} for {damage} damage!")
        elif choice == "2":
            print(f"{player.name} defends and reduces damage this turn.")
        else:
            print("Invalid choice, you lose your turn!")

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
    else:
        print(f"\n{RED}{player.name} has been defeated...{RESET}")


# Example game loop
player = Player("Hero")

while player.is_alive():
    # Create enemy with scaled stats based on player level
    goblin = Enemy("Goblin", 30, 8, 3, 10, player.level)
    battle(player, goblin)
    if not player.is_alive():
        break
    print("\nDo you want to continue adventuring? (y/n)")
    cont = input("> ").lower()
    if cont != "y":
        print("Thanks for playing!")
        break