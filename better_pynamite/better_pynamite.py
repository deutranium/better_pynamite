import random
import sys


def chaos(p=0.5):
    rand = random.random()

    if rand <= p:
        sys.exit("Gotcha!")
    else:
        print("Today is your lucky day.")
    return 0


chaos(p=0.5)
