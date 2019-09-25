from os import system, name
from random import randint
from time import sleep

def clear():
    _ = system('clear' if name =='posix' else 'cls')

def user_plays():
    while True:
        clear()
        print('Runs = {}'.format(runs))
        print('Choose a number: ', end='')
        num = int(input())
        if num in range(7):
            return num
        else:
            print('Illegal move')

def comp_plays():
    num = randint(0,6)
    print('Computer plays {}'.format(num))
    return num

def increment_runs(num):
    global runs
    runs += num

def get_out():
    global out
    out = True
    print('Out!')
    print('Total = {}'.format(runs))

runs = 0
out = False

while not out:
    clear()
    player = user_plays()
    comp = comp_plays()
    if player == comp:
        get_out()
    else:
        increment_runs(player)
    sleep(1)
