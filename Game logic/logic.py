from os import system, name
from random import randint
from time import sleep

def clear():
    _ = system('clear' if name =='posix' else 'cls')

def stay(seconds=1):
    sleep(seconds)

def display_header(innings_number, runs, is_user_batting, target):
    clear()
    print('Innings {}'.format(innings_number).upper())
    print('{}ing\n'.format(innings_map[is_user_batting]).upper())
    print('Runs = {}'.format(runs))
    if target != -1:
        print('Target = {}'.format(target))
        print('{} runs required to win'.format(target - runs))
    print()

def user_plays():
    while True:
        print('Choose a number: ', end='')
        num = int(input().strip())
        if num in range(7):
            return num
        else:
            print('Illegal move')

def comp_plays(num=-1):
    if num == -1:
        num = randint(0,6)
    print('Computer plays {}'.format(num))
    return num

def increment_runs(runs, num):
    runs += num
    return runs

def assign_runs(runs, is_user_batting):
    if is_user_batting:
        global user_runs
        user_runs = runs
    else:
        global comp_runs
        comp_runs = runs

def out():
    is_out = True
    print('Out!')
    return is_out

def end_innings(runs, is_user_batting):
    print('Total = {}'.format(runs))
    assign_runs(runs, is_user_batting)

def get_target(is_user_batting):
    target = -1
    if is_user_batting:
        global comp_runs
        target = comp_runs + 1
    else:
        global user_runs
        target = user_runs + 1
    return target

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
        print('Choose batting(1) or bowling(2): ', end='')
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
    target = -1
    if innings_number == 2:
        target = get_target(is_user_batting)
    clear()
    print('Get ready to {}'.format(innings_map[is_user_batting]))
    for i in range(3, 0, -1):
        print('{}...  '.format(i), end='', flush=True)
        stay()
    runs = 0
    is_out = False
    has_won_by_runs = True
    while not is_out:
        display_header(innings_number, runs, is_user_batting, target)
        user = user_plays()
        comp = comp_plays(3)
        if user == comp:
            is_out = out()
            end_innings(runs, is_user_batting)
        else:
            if is_user_batting:
                runs = increment_runs(runs, user)
            else:
                runs = increment_runs(runs, comp)
        if innings_number == 2 and runs >= target:
            end_innings(runs, is_user_batting)
            is_out = True
            has_won_by_runs = False
        stay()
    return runs, has_won_by_runs

def declare_winner(has_won_by_runs=True):
    global user_runs
    global comp_runs
    clear()
    diff = user_runs - comp_runs
    msg = ''
    if diff == 0:
        print('It is a TIE')
        return
    if diff > 0:
        print('Congratulations!!')
        msg = 'You win'
    else:
        print('Better luck next time.')
        msg ='Comp wins'
        diff *= -1
    if has_won_by_runs:
        print('{} by {} runs'.format(msg, diff))
    else:
        print('{} by 1 wicket'.format(msg))

innings_map = {True: 'bat', False: 'bowl'}
user_runs = 0
comp_runs = 0

def main():
    is_user_batting = toss()
    _, _ = innings(is_user_batting, 1)
    is_user_batting = not is_user_batting
    _, has_won_by_runs = innings(is_user_batting, 2)
    declare_winner(has_won_by_runs)

if __name__ == '__main__':
    main()
