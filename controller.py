import view

def start():
    view.start_view()
    i = input()
    if i == 'y':
        return view.start_game()
    else:
        return view.end_view()
