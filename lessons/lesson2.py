#Родительский класс:
class Hero:
    """Класс героя"""
    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты объекта|экземпляра класса
        self.hero_name = name
        self.hero_lvl = lvl
        self.hero_hp = hp

    def base_action(self):
        print(f"{self.hero_name} base action!!")


#ДОчерний класс:
class MageHero(Hero):
