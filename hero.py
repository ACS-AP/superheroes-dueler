from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        self.abilities = list()
        self.armors = list()

        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        damage_taken = max(damage - defense, 0)
        self.current_health -= damage_taken

    def is_alive(self):
        return self.current_health > 0

    def fight(self, opponent):
        if (len(self.abilities) == 0) and (len(opponent.abilities) == 0):
            print("It's a draw!")

            # Prevent endless loop by setting each health to 0
            opponent.current_health = 0
            self.current_health = 0
        else:
            while True:
                attack_damage = self.attack()
                opponent.take_damage(attack_damage)

                opponent_attack_damage = opponent.attack()
                self.take_damage(opponent_attack_damage)

                if not opponent.is_alive() and not self.is_alive():
                    print("It's a draw!")

                    opponent.add_death(1)
                    opponent.add_kill(1)

                    self.add_death(1)
                    self.add_kill(1)
                    break
                elif not opponent.is_alive():
                    print(f"{self.name} has won")
                    opponent.add_death(1)
                    self.add_kill(1)
                    break
                elif not self.is_alive():
                    print(f"{opponent.name} has won")
                    self.add_death(1)
                    opponent.add_kill(1)
                    break

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())