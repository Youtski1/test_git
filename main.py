import random


def random_number(n1: int, n2: int) -> int:
    """return: random number"""
    return random.randint(n1,n2)


print(random_number(0,100))