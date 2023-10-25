#Welcome to the game "The Oregon Trail"!

class Character: #все игровые персонажи

    def __init__(self, first_name = 'Person', health_num = 5, mood_num = 5, energy_num = 5, clean_num = 5, main_profession = None, first_trait = None, second_trait = None):
        self.name = first_name
        self.health_lvl = health_num
        self.mood_lvl = mood_num
        self.energy_lvl = energy_num
        self.clean_lvl = clean_num
        self.profession = main_profession
        self.trait1 = first_trait
        self.trait2 = second_trait

class Wagon: #повозка

    def __init__(self, size_num = 36, tools_col = 0, meat_col = 0, medicine_col = 0, clothes_col = 0, bullets_col = 0, coffee_col = 0):
        self.size = size_num
        self.tools = tools_col
        self.meat = meat_col
        self.medicine = medicine_col
        self.clothes = clothes_col
        self.bullets = bullets_col
        self.coffee = coffee_col

class Events: #события, происходящие на протяжении маршрута группы

    def __init__(self, storyline = False, frequency = 0, positive = True, changing_traits = False, optional = True):
        self.is_storyline = storyline
        self.is_frequency = frequency
        self.is_positive = positive
        self.is_changing_traits = changing_traits
        self.is_optional = optional

first_p = Character('Lorens', 5, 5, 6, 5, 'fisherman', 'neat', 'sporting')
print(first_p.__dict__)
second_p = Character('Amy', 5, 5, 4, 5, 'missionary', 'charming', 'religious')
print(second_p.__dict__)
third_p = Character('Elisa', 5, 5, 5, 3, 'mountain woman', 'egocentric', 'untidy')
print(third_p.__dict__)
fourth_p = Character('Hatty', 3, 5, 4, 4, 'doctor', 'silly', 'charming')
print(fourth_p.__dict__)

print()

wagon1 = Wagon(54, 3, 2, 2, 2, 50, 4)
print(wagon1.__dict__)
wagon2 = Wagon(36, 1, 1, 1, 2, 25, 2)
print(wagon2.__dict__)
wagon3 = Wagon(36, 3, 2, 3, 4, 25, 2)
print(wagon3.__dict__)

print()

meet_with_hunter = Events(True, 1, True, False, True)
print(meet_with_hunter.__dict__)
rain_day = Events(False, 5, False, True, False)
print(rain_day.__dict__)
help_to_soldiers = Events(True, 2, True, False, True)
print(help_to_soldiers.__dict__)

print()
print('Example of side effect of passing objects by reference')

wagon4 = wagon2
print('first output of wagon4', wagon4.__dict__)
print('first output of wagon2', wagon2.__dict__)
wagon4.bullets = 50
setattr(wagon4, 'meat', 2)
print('the result of wagon4 after changing wagon4', wagon4.__dict__)
print('the result of wagon2 after changing wagon4', wagon2.__dict__)
