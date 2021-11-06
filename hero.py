from os import name
from ability import Ability
from armor import Armor
from weapon import Weapon
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, incoming_damage):
        for armor in self.armors:
            incoming_damage -= armor.block()

        return incoming_damage

    def take_damage(self, damage):
        remaining_damage = self.defend(damage)
        if remaining_damage <= 0:
            return f'No damage was taken. {self.name} has {self.current_health} health remaining.'
        else:
            self.current_health = self.current_health - remaining_damage
            return f'{self.name} took {remaining_damage} points in damage. {self.name} has {self.current_health} health remaining.'

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def fight(self, opponent):
        
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            return 'Draw'
        else:
            while self.is_alive() == True and opponent.is_alive() == True:  
                print(f'{self.name} and {opponent.name} attack!')
                print(opponent.take_damage(self.attack()))
                print(self.take_damage(opponent.attack()))
                if self.is_alive() == True and opponent.is_alive() == False:
                    self.add_kill(1)
                    opponent.add_death(1)
                    return f'{self.name} defeated {opponent.name}!'
                elif opponent.is_alive() == True and self.is_alive() == False:
                    opponent.add_kill(1)
                    self.add_death(1)
                    return f'{opponent.name} defeated {self.name}!'
                elif self.is_alive() == False and opponent.is_alive() == False:
                    self.add_kill(1)
                    self.add_death(1)
                    opponent.add_kill(1)
                    opponent.add_death(1)
                    return f'{self.name} and {opponent.name} defeated eachother. Draw!'
                else:
                    continue
        
        # heros = [self.name, opponent.name]
        # winner = random.choice(heros)
        # if winner == heros[0]:
        #     return f'{winner} defeats {heros[1]}'
        # elif winner == heros[1]:
        #     return f'{winner} defeats {heros[0]}'



if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  grace = Hero("Grace Hopper", 200)
  print(grace.name)
  print(grace.current_health)
  antman = Hero("Antman")
  print(grace.fight(antman))

  debugging = Ability("Great Debugging", 50)
  shock = Ability("Shock", 20)
  grace.add_ability(debugging)
  grace.add_ability(shock)
  print(grace.abilities)
  print(grace.attack())
  iron_man_suit = Armor("Iron Man Suit", 50)
  helmet = Armor("helmet", 15)
  chestplate = Armor("chestplate", 30)
  gloves = Armor("Super Gloves", 50)
  grace.add_armor(gloves)
  grace.add_armor(helmet)
  print(grace.armors)
#   print(grace.current_health)
  print(grace.defend(100))
  print(grace.take_damage(50))
  print(grace.is_alive())
  print(grace.take_damage(15000))
  print(grace.is_alive())

  print(len(grace.abilities))

  superman = Hero("Superman", 200)
  antman.add_ability(shock)

  print(superman.fight(antman))

  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")
  ability1 = Ability("Super Speed", 300)
  ability2 = Ability("Super Eyes", 130)
  ability3 = Ability("Wizard Wand", 80)
  ability4 = Ability("Wizard Beard", 20)
  hero1.add_ability(ability1)
  hero1.add_ability(ability2)
  hero2.add_ability(ability3)
  hero2.add_ability(ability4)
  print(hero1.fight(hero2))

  hero = Hero("Wonder Woman")
  weapon = Weapon("Lasso of Truth", 90)
  hero.add_weapon(weapon)
  print(hero.attack())