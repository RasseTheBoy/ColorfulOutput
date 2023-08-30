
from FastDebugger import fd


def loop(t):
    def get_values(_t) -> list[int]:
        _t = _t[2:].split('m')[0]
        return [int(x) for x in _t.split(';')]
            
            
    for char_indx, char in enumerate(t):
        if char != '\033':
            continue

        values_lst = get_values(t[char_indx:])

        if len(values_lst) == 1: # End of ANSI escape sequence
            print('End of ANSI escape sequence')

        else:
            print(f'Start of ANSI escape sequence; with values: {values_lst}')


# t = '\x1b[91;4m\x1b[91mHello world!\x1b[0m\x1b[0m'
t = '\033[91;4mHello world!\033[0m'

loop(t)