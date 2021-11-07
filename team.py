class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero_name):
        self.heroes.append(hero_name)

    def remove_hero(self, hero_name):
        foundHero = False

        for hero in self.heroes:
            if hero.name == hero_name:
                self.heroes.remove(hero)
                foundHero = True

        if not foundHero:
            return 0


    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name) 