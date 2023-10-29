#Welcome to the game "The Oregon Trail"!

class Character: #все игровые персонажи

    def __init__(self, first_name = 'Person', health_num = 5, mood_num = 5, energy_num = 5, clean_num = 5):
        self.name = first_name
        self.health_lvl = health_num
        self.mood_lvl = mood_num
        self.energy_lvl = energy_num
        self.clean_lvl = clean_num

    def progress_health_lvl(self, num: int):
        if (self.health_lvl < 6) and ((self.health_lvl + num) <= 6):
            self.health_lvl += num
            return (f'Health level: {self.health_lvl}')
        else:
            return (f'Impossible')

    def progress_mood_lvl(self, num: int):
        if (self.mood_lvl < 6) and ((self.mood_lvl + num) <= 6):
            self.mood_lvl += num
            return (f'Mood level: {self.mood_lvl}')
        else:
            return (f'Impossible')

    def progress_clean_lvl(self, num: int):
        if (self.clean_lvl < 6) and ((self.clean_lvl + num) <= 6):
            self.clean_lvl += num
            return (f'Clean level: {self.clean_lvl}')
        else:
            return (f'Impossible')

    def progress_energy_lvl(self, num: int):
        if (self.energy_lvl < 6) and ((self.energy_lvl + num) <= 6):
            self.energy_lvl += num
            return (f'Energy level: {self.energy_lvl}')
        else:
            return (f'Impossible')

class Wagon: #повозка

    def __init__(self, size_num = 36, tools_col = 0, meat_col = 0, medicine_col = 0, clothes_col = 0, bullets_col = 0, coffee_col = 0):
        self.size = size_num
        self.tools = tools_col
        self.meat = meat_col
        self.medicine = medicine_col
        self.clothes = clothes_col
        self.bullets = bullets_col
        self.coffee = coffee_col

    def check_fullness(self):
        return ((False, True)[self.size < (self.tools + self.meat + self.medicine + self.clothes + self.bullets + self.coffee)])

    def add_new_tools(self, num: int):
        self.tools += num
        if not self.check_fullness:
            self.tools -= num
            return (f'Item doesn\'t fit')
        return (f'Item has added')

    def add_new_meat(self, num: int):
        self.meat += num
        if not self.check_fullness:
            self.meat -= num
            return (f'Item doesn\'t fit')
        return (f'Item has added')

    def add_new_medicine(self, num: int):
        self.medicine += num
        if not self.check_fullness:
            self.medicine -= num
            return (f'Item doesn\'t fit')
        return (f'Item has added')

    def add_new_clothes(self, num: int):
        self.clothes += num
        if not self.check_fullness:
            self.clothes -= num
            return (f'Item doesn\'t fit')
        return (f'Item has added')

    def add_new_bullets(self, num: int):
        self.bullets += num
        if not self.check_fullness:
            self.bullets -= num
            return (f'Item doesn\'t fit')
        return (f'Item has added')

    def add_new_coffee(self, num: int):
        self.coffee += num
        if not self.check_fullness:
            self.coffee -= num
            return (f'Item doesn\'t fit')
        return (f'Item has added')

first_p = Character('Lorens', 2, 5, 6, 5)
print(first_p.__dict__)
second_p = Character('Amy', 5, 2, 4, 1)
print(second_p.__dict__)
third_p = Character('Elisa', 5, 1, 1, 3)
print(third_p.__dict__)
fourth_p = Character('Hatty', 2, 5, 4, 4)
print(fourth_p.__dict__)

print()

wagon1 = Wagon(54, 20, 18, 4, 2, 6, 2)
print(wagon1.__dict__)
wagon2 = Wagon(36, 1, 1, 10, 2, 15, 2)
print(wagon2.__dict__)
wagon3 = Wagon(36, 0, 10, 0, 0, 11, 1)
print(wagon3.__dict__)

print('Let\'s use some methods')

print(first_p.progress_mood_lvl(2))
print(fourth_p.progress_health_lvl(1))
print(third_p.progress_energy_lvl(5))
print(wagon1.add_new_bullets(10))
print(wagon2.add_new_meat(2))
print(wagon3.add_new_medicine(6))
