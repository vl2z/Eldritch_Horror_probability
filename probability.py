# -*- coding: utf-8 -*-
from math import factorial


def c(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


# Bernoulli formula
def bern(n, k, p):
    return c(n, k) * p ** k * (1 - p) ** (n - k)


def win_probability(human_strength, monster_toughness, probability):
    ans = 0
    for i in range(monster_toughness, human_strength + 1):  # sum prob from initial to max chance
        ans += bern(human_strength, i, probability)
    return ans * 100  # percent


# just in case we don't want to calculate initial probability ourselves
def monster_range(human_strength, monster_toughness, success=None, failure=None):
    if success is None:
        success = [5, 6]
    if failure is None:
        failure = [1, 2, 3, 4]
    probability = len(success) / (len(success) + len(failure))
    return win_probability(human_strength, monster_toughness, probability)


# find probability if can roll only one die
def one_success_at_least(number_of_dice, probability=2 / 6):
    # return win_probability(number_of_dice, 1, probability)
    return (1 - bern(number_of_dice, 0, probability)) * 100  # these are equal, but latter costs less


strength = int(input("Enter human strength (сила): "))
toughness = int(input("Enter monster toughness (стойкость): "))
enter_probability = input("Default probability set for [5, 6] as success.\n Change probability (y/n)? ")

if enter_probability != 'n':
    try:
        probability = float(eval(input("Enter new value (ex. 1/6): ")))
    except:  # eval and except all are security flaw
        print("Unable to set new value. Default value is used.")
        probability = 2 / 6
else:
    probability = 2 / 6

print("Probability to win: {} %".format(win_probability(strength, toughness, probability)))
