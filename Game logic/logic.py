from os import system, name
from random import randint
from time import sleep

def clear():
    _ = system('clear' if name =='posix' else 'cls')

runs = 0
out = False

while not out:
    clear()
    print('Runs = {}'.format(runs))
    print('Choose a number: ', end='')
    player = int(input())
    if player not in range(7):
        print('Illegal move')
    else:
        comp = randint(0,6)
        print('Computer plays {}'.format(comp))
        if player == comp:
            print('Out!')
            print('Total = {}'.format(runs))
            out = True
        else:
            runs += player
        sleep(1)
