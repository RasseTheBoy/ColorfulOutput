

class ANSI:
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLACK = '\033[90m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    ENDC = '\033[0m'


print(f'{ANSI.RED}{ANSI.BOLD}Hello world! {ANSI.UNDERLINE}Here we are again!{ANSI.ENDC}')