
from FastDebugger import fd


ANSI_color_range = [x for x in range (90, 97)]
ANSI_modif_range = [1,4]


if __name__ == '__main__':
    l = [91, 1, 4, 95]

    l = [x for x in l if x not in ANSI_color_range]

    fd(l)