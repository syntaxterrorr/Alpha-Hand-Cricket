import view

def start():
    view.start_view()
    input = input()
    if input == 'y':
        return view.start_game()
    else:
        return view.end_view()
