class Hero:
    def __init__(self, name, lvl, hp, strenght):
        self.hero_name = name
        self.hero_lvl = lvl
        self.hero_hp = hp
        self.hero_strength = strenght

    def greet(self):
        print(f"Hi, I'm {self.hero_name}, my lvl is {self.hero_lvl}!")

    def attack(self):
        print(f'{self.hero_name} attacks')
        self.hero_hp -= 10
        self.hero_strength -= 100

    def rest(self):
        print(f'{self.hero_name} rests')
        self.hero_hp += 10
        self.hero_strength += 100

iron_man = Hero('Iron man', 100, 100, 1000)
deadpool = Hero('Deadpool', 100, 100, 1000)

#Iron man
print("Before: ", iron_man.hero_name, "health: ", iron_man.hero_hp,",", "strength: ", iron_man.hero_strength )
iron_man.greet()
iron_man.attack()
print("Health: ", iron_man.hero_hp)
print("Strength: ", iron_man.hero_strength)
iron_man.rest()
print("After:", iron_man.hero_name, "health:", iron_man.hero_hp,",", "strength:", iron_man.hero_strength )

print()

#Deadpool
print("Before:", deadpool.hero_name, "health: ", deadpool.hero_hp,",", "strength: ", deadpool.hero_strength )
deadpool.greet()
deadpool.attack()
print("Health: ", deadpool.hero_hp)
print("Strength: ", deadpool.hero_strength)
deadpool.rest()
print("After:", deadpool.hero_name, "health:", deadpool.hero_hp,",", "strength:", deadpool.hero_strength )

print()
