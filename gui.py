import curses
import main

"""Menu"""
def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    options = [
        ["Option 1.1", "Option 1.2", "Option 1.3"],
        ["Option 2.1", "Option 2.2", "Option 2.3"],
        ["Option 3.1", "Option 3.2", "Option 3.3"],
    ]

    logo = """
 __    __  __                __        __            _______               __     
/  \  /  |/  |              /  |      /  |          /       \             /  |    
$$  \ $$ |$$/  _____  ____  $$ |____  $$ |  ______  $$$$$$$  |  ______   _$$ |_   
$$$  \$$ |/  |/     \/    \ $$      \ $$ | /      \ $$ |__$$ | /      \ / $$   |  
$$$$  $$ |$$ |$$$$$$ $$$$  |$$$$$$$  |$$ |/$$$$$$  |$$    $$< /$$$$$$  |$$$$$$/   
$$ $$ $$ |$$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$    $$ |$$$$$$$  |$$ |  $$ |  $$ | __ 
$$ |$$$$ |$$ |$$ | $$ | $$ |$$ |__$$ |$$ |$$$$$$$$/ $$ |__$$ |$$ \__$$ |  $$ |/  |
$$ | $$$ |$$ |$$ | $$ | $$ |$$    $$/ $$ |$$       |$$    $$/ $$    $$/   $$  $$/ 
$$/   $$/ $$/ $$/  $$/  $$/ $$$$$$$/  $$/  $$$$$$$/ $$$$$$$/   $$$$$$/     $$$$/  

    """
    print(logo)
    current_page = 0
    current_option = 0
    while True:
        stdscr.clear()
        stdscr.addstr(logo, curses.color_pair(1))
        stdscr.addstr("Page " + str(current_page + 1) + "\n")
        stdscr.addstr("Select an option:\n")
        for i, option in enumerate(options[current_page]):
            if i == current_option:
                stdscr.addstr(option + "\n", curses.color_pair(2))
            else:
                stdscr.addstr(option + "\n", curses.color_pair(1))

        c = stdscr.getch()
        if c == curses.KEY_UP:
            current_option = max(current_option - 1, 0)
        elif c == curses.KEY_DOWN:
            current_option = min(current_option + 1, len(options[current_page]) - 1)
        elif c == curses.KEY_LEFT:
            current_page = max(current_page - 1, 0)
            current_option = 0
        elif c == curses.KEY_RIGHT:
            current_page = min(current_page + 1, len(options) - 1)
            current_option = 0
        elif c == 10: # ASCII value of '\n'
            stdscr.clear()        
            stdscr.addstr(logo, curses.color_pair(1))                                                          
            stdscr.addstr("Selected option: " + options[current_page][current_option])
            stdscr.refresh()
            stdscr.getch()
            break


curses.wrapper(main)

"""============================================================================"""