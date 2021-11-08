from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

import sys
import os

def input_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid Input!")
            continue

def calc_kd(team):
    team_kills = 0
    team_deaths = 0

    for hero in team.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    return team_kills / team_deaths

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("What is the ability name?\n")
        max_damage = input_int("What is the max damage of the ability?\n")
        clear()

        return Ability(name, max_damage)

    def create_weapon(self):
        weapon_name = input("What is the weapon name?\n")
        weapon_damage = input_int("What is the weapon damage?\n")
        clear()

        return Weapon(weapon_name, weapon_damage)

    def create_armor(self):
        name = input("What is the armor name?\n")
        max_block = input_int("What is the max block for the armor?\n")
        clear()

        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")

        hero = Hero(hero_name)
        add_item = None
        while add_item != 4:
            clear()
            add_item = input_int(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            clear()
            if add_item == 1:
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == 2:
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == 3:
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        team_name = input("What would you like team one's name to be?\n")
        clear()

        self.team_one = Team(team_name)

        number_of_team_members = input_int("How many members would you like on Team One?\n")
        clear()

        for i in range(number_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        team_name = input("What would you like team two's name to be?\n")
        clear()

        self.team_two = Team(team_name)
        number_of_team_members = input_int("How many members would you like on Team Two?\n")
        clear()

        for i in range(number_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        clear()
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        team_one_kd = calc_kd(self.team_one)
        print(self.team_one.name + " average K/D was: " + str(team_one_kd))

        team_two_kd = calc_kd(self.team_two)
        print(self.team_two.name + " average K/D was: " + str(team_two_kd))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("Survived from " + self.team_one.name + ": " + hero.name)

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

def main():
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    print("The fight has started!")
    while True:
        arena.team_battle()
        arena.show_stats()

        new_game = input("Do you want to play again? ")
        clear()

        if new_game.lower() != "yes":
            break
        arena.team_one.revive_heroes()
        arena.team_two.revive_heroes()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
