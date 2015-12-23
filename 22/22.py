import random


class Character:
    def __init__(self, HP=0, base_damage=0, base_armor=0):
        self.HP = int(HP)
        self._base_damage = int(base_damage)
        self._base_armor = int(base_armor)
        self.charge = 0
        self.shield = 0
        self.poison = 0
        self.mana = 500
        self.spent_mana = 0
        
    @property
    def damage(self):
        return self._base_damage

    @property
    def armor(self):
        return self._base_armor + 7 if self.shield else 0
                 
                 
    def hit(self, other):
        other.HP -= max(self.damage - other.armor, 1)
       
    def is_living(self):
        if self.HP > 0:
            return True
        else:
            return False
    
    def update(self):
        if self.shield:
            self.shield -= 1
        if self.charge:
            self.charge -= 1
            self.mana += 101
        if self.poison:
            self.poison -= 1
            self.HP -= 3


class Hero(Character):


    def hit(self, other):
        if self.mana < 53:
            return False
        
        choice = random.randint(0,4)
        if choice == 0:
            self.mm(other)
        elif choice == 1:
            self.drain(other)
        elif choice == 2:
            self.mshield(other)
        elif choice == 3:
            self.mpoison(other)
        elif choice == 4:
            self.mcharge(other)
    
    def mm(self, other):
        self.mana -= 53
        self.spent_mana += 53
        other.HP -= 4
        
    def drain(self, other):
        if self.mana < 73:
            self.hit(other)
        else:
            self.mana -= 73
            self.spent_mana += 73
            self.HP += 2
            other.HP -= 2
            
    def mshield(self, other):
        if self.mana < 113:
            self.hit(other)
        elif self.shield:
            self.hit(other)
        else:
            self.mana -= 113
            self.spent_mana += 113
            self.shield = 6
            
    def mpoison(self, other):
        if self.mana < 173:
            self.hit(other)
        elif other.poison:
            self.hit(other)
        else:
            self.mana -= 173
            self.spent_mana += 173
            other.poison = 6  
            
    def mcharge(self, other):
        if self.mana < 229:
            self.hit(other)
        elif self.charge:
            self.hit(other)
        else:
            self.mana -= 229
            self.spent_mana += 229
            self.charge = 6
            
class CombatSimulator:
    def __init__(self, hero=None, villain=None):
        self.hero = hero
        self.villain = villain
    
    
    def run(self):
        while True:
            self.hero.update()
            self.villain.update()
            if not self.villain.is_living():
                #print("Hero Wins!")
                return self.hero.spent_mana
                
            self.hero.hit(self.villain)
            if not self.villain.is_living():
                #print("Hero Wins!")
                return self.hero.spent_mana
                
            self.hero.update()
            self.villain.update()
            if not self.villain.is_living():
                #print("Hero Wins!")
                return self.hero.spent_mana
                
            self.villain.hit(self.hero)
            if not self.hero.is_living():
                #print("Hero Loses :(")
                return False
                
    def run2(self):
        while True:
            self.hero.HP -= 1
            if not self.hero.is_living():
                return False
                
            self.hero.update()
            self.villain.update()   
            if not self.villain.is_living():
                return self.hero.spent_mana
                
            self.hero.hit(self.villain)
            if not self.villain.is_living():
                return self.hero.spent_mana
            
            self.hero.HP -= 1
            if not self.hero.is_living():
                return False
                
            self.hero.update()
            self.villain.update()
            if not self.villain.is_living():
                return self.hero.spent_mana
                
            self.villain.hit(self.hero)
            if not self.hero.is_living():
                return False

min_mana = 10**7
wins = 0
while wins < 10**0:
    boss = Character(HP=55, base_damage=8)
    player = Hero(HP=50)
    battle = CombatSimulator(hero=player, villain=boss)
    result = battle.run()
    if result:
        wins += 1
        min_mana = min(min_mana, result)
        
print(min_mana)

min_mana_2 = 10**7
wins2 = 0

while wins2 < 10**4:
    boss = Character(HP=55, base_damage=8)
    player = Hero(HP=50)
    battle = CombatSimulator(hero=player, villain=boss)
    result2 = battle.run2()
    if result2:
        wins2 += 1
        min_mana_2 = min(min_mana_2, result2)
print(min_mana_2)