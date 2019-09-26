from os import system, name
from random import randint
from time import sleep

def clear():
    _ = system('clear' if name =='posix' else 'cls')

def stay(seconds=1):
    sleep(seconds)

def display_header(innings_number, runs, is_user_batting):
    clear()
    print('Innings {}'.format(innings_number).upper())
    print('{}ing\n'.format(innings_map[is_user_batting]).upper())
    print('Runs = {}'.format(runs))

def user_plays():
    while True:
        print('Choose a number: ', end='')
        num = int(input().strip())
        if num in range(7):
            return num
        else:
            print('Illegal move')

def comp_plays():
    num = randint(0,6)
    print('Computer plays {}'.format(num))
    return num

def increment_runs(runs, num):
    runs += num
    return runs

def assign_runs(runs, is_user_batting):
    global user_runs
    global comp_runs
    if is_user_batting:
        user_runs = runs
    else:
        comp_runs = runs


def out(runs, is_user_batting):
    is_out = True
    print('Out!')
    print('Total = {}'.format(runs))
    assign_runs(runs, is_user_batting)
    return is_out

def toss():
    clear()
    print('TOSS')
    choice_map = {'o': True, 'odd': True, '1':True, 'e': False, 'even': False, 'eve': False, '2': False}
    print('Choose odd(o) or even(e): ', end='')
    choice = choice_map[input().strip()]
    winner_map = {choice: 'user', not choice: 'comp'}
    user = user_plays()
    comp = comp_plays()
    is_user_batting = True
    a = ''
    b = ''
    global innings_map
    if winner_map[(user + comp) % 2] == 'user':
        selection_map = {'batting': True, 'bat': True, '1':True, 'bowling': False, 'bowl': False, '2':False}
        print('You win the toss!')
        print('Choose batting(1) or bowling(2): ')
        is_user_batting = selection_map[input().strip()]
        a = 'You choose'
        b = innings_map[is_user_batting]
    else:
        is_user_batting = bool(randint(0,1))
        print('Comp wins the toss.')
        a = 'Comp chooses'
        b = innings_map[not is_user_batting]
    print('{} to {} first.'.format(a, b))
    stay()
    return is_user_batting
    


def innings(is_user_batting, innings_number):
    global innings_map
    clear()
    print('Get ready to {}'.format(innings_map[is_user_batting]))
    for i in range(3, 0, -1):
        print('{}...  '.format(i), end='', flush=True)
        stay()
    runs = 0
    is_out = False
    while not is_out:
        display_header(innings_number, runs, is_user_batting)
        user = user_plays()
        comp = comp_plays()
        if user == comp:
            is_out = out(runs, is_user_batting)
        else:
            runs = increment_runs(runs, user)
        stay()
    return runs

def declare_winner():
    global user_runs
    global comp_runs
    clear()
    diff = user_runs - comp_runs
    msg = ''
    if diff > 0:
        print('Congratulations!!')
        msg = 'You win'
    else:
        print('Better luck next time.')
        msg ='Comp wins'
        diff *= -1
    print('{} by {} runs'.format(msg, diff))

innings_map = {True: 'bat', False: 'bowl'}
user_runs = 0
comp_runs = 0

def main():
    is_user_batting = toss()
    _ = innings(is_user_batting, 1)
    is_user_batting = not is_user_batting
    _ = innings(is_user_batting, 2)
    declare_winner()

if __name__ == '__main__':
    main()
