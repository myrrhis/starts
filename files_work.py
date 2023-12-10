from random import randint


class Cat:
    def __init__(self, name, weight, fq):
        self.name = name
        self.weight = weight
        self.fq = fq


def create_ten_files():
    for number in range(1, 11):
        ls = [randint(1, 100) for _ in range(3)]
        with open(f'{number}.txt', 'wt') as f:
            f.write(f'{ls[0]}\n{ls[1]}\n{ls[2]}\n')

def two_files_sum(x, y):
    ls = []
    x_and_y = [x, y]
    for i in x_and_y:
        with open(f'{i}.txt') as f:
            for line in f:
                ls.append(int(line.rstrip('\n')))
    return sum(ls)

def create_cats(filename):
    cats = []
    with open(filename) as f:
        for line in f:
            ls = line.rstrip('\n').split()
            name = ls[0]
            weight = float(ls[1])
            fq = int(ls[2])
            cats.append(Cat(ls[0], float(ls[1]), int(ls[2])))
    return cats

create_ten_files()
print(two_files_sum(5, 9))

for cat in create_cats('cat.txt'):
    print(cat.name, cat.weight, cat.fq)
