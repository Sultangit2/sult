class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        print(f"Hero's name: {self.name}")

    def multiply_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}\nSuperpower: {self.superpower}\nHealth points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("Сайтама", "One Punch Man", "Бесподобная сила", 1000,
                 "Завтрашние заботы пускай останутся завтрашнему мне")
hero.display_name()
hero.multiply_health()
print(hero)
print("Length of catchphrase:", len(hero))