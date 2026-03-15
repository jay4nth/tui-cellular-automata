from random import random

def generate_random(width, height):
    random_set=set()
    for i in range(width):
        for j in range(height):
            if random()<0.3:
                random_set.add((i,j))
    return random_set