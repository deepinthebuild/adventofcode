import itertools as it

class Item:
    def __init__(self, name='foo', cost=None, damage=None, armor=None):
        self.name = name
        self.cost = int(cost)
        self.damage = int(damage)
        self.armor = int(armor)
        
    def __repr__(self):
        return self.name

class Character:
    def __init__(self, HP=0, base_damage=0, base_armor=0, inventory=[]):
        self.HP = int(HP)
        self._base_damage = int(base_damage)
        self._base_armor = int(base_armor)
        self.inventory = list(inventory)

    @property
    def damage(self):
        return self._base_damage + sum(item.damage for item in self.inventory)

    @property
    def armor(self):
        return self._base_armor + sum(item.armor for item in self.inventory)
        
    @property
    def cost(self):
        return sum(item.cost for item in self.inventory)
               
    def hit(self, other):
        other.HP -= self.damage - other.armor
       
    def is_living(self):
        if self.HP > 0:
            return True
        else:
            return False
    
class CombatSimulator:
    def __init__(self, hero=None, villain=None):
        self.hero = hero
        self.villain = villain
    
    
    def run(self):
        while True:
            self.hero.hit(self.villain)
            if not self.villain.is_living():
                print("Hero Wins!")
                print("Total Cost: ", self.hero.cost)
                return True
                
            self.villain.hit(self.hero)
            if not self.hero.is_living():
                return False
                
    def run2(self):
        while True:
            self.hero.hit(self.villain)
            if not self.villain.is_living():
                return False

            self.villain.hit(self.hero)
            if not self.hero.is_living():
                print("Villain Wins!")
                print("Total Cost: ", self.hero.cost)
                return True

def total_cost(list_of_items):
    return sum(item.cost for item in list_of_items)
    
    
boss_stats = {}
with open("input.txt", "r") as input:
    for line in input:
        k, v = line.split(": ")
        boss_stats[k] = v

Weapons = []
Rings = []
Armor = []

with open("weapons.txt", "r") as input:
    for line in input:
        name, cost, dam, armor = line.split()
        Weapons.append(Item(name=name, cost=cost, damage=dam, armor=armor))
        
with open("rings.txt", "r") as input:
    for line in input:
        name, cost, dam, armor = line.split()
        Rings.append(Item(name=name, cost=cost, damage=dam, armor=armor))
        
with open("armor.txt", "r") as input:
    for line in input:
        name, cost, dam, armor = line.split()
        Armor.append(Item(name=name, cost=cost, damage=dam, armor=armor))
        
Equipment = it.product(Weapons, Armor, it.combinations(Rings, 2))
Equipment = [(a,) + (b,) + c for a,b,c in Equipment]
Equipment = sorted(Equipment, key=total_cost)

for equip_set in Equipment:
    player = Character(HP = 100, base_damage = 0, 
                        base_armor = 0, inventory = equip_set)
    boss = Character(HP = boss_stats["Hit Points"], 
                        base_damage = boss_stats["Damage"],
                        base_armor = boss_stats["Armor"])
    battle = CombatSimulator(hero=player, villain=boss)
    if battle.run():
        break
        
Equipment = sorted(Equipment, key=total_cost, reverse=True)

for equip_set in Equipment:
    player = Character(HP = 100, base_damage = 0, 
                        base_armor = 0, inventory = equip_set)
    boss = Character(HP = boss_stats["Hit Points"], 
                        base_damage = boss_stats["Damage"],
                        base_armor = boss_stats["Armor"])
    battle = CombatSimulator(hero=player, villain=boss)
    if battle.run2():
        break
            
    