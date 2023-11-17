from pack_2.summator import summator


def addition(x, amount):
    for i in range(amount):
        x = summator(x)
    return x
