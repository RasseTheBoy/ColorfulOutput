
from typing import Any


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def HEADER(text:Any) -> str:
    """Returns the text with the header color

    Parameters
    ----------
    text : Any
        The text to be colored
    
    Returns
    -------
    str
        The colored text"""
    return bcolors.BLUE + str(text) + bcolors.ENDC


def BLUE(text:Any) -> str:
    """Returns the text with the blue color
    
    Parameters
    ----------
    text : Any
        The text to be colored
    
    Returns
    -------
    str
        The colored text"""
    return bcolors.BLUE + str(text) + bcolors.ENDC


def CYAN(text:Any) -> str:
    """Returns the text with the cyan color
    
    Parameters
    ----------
    text : Any
        The text to be colored
    
    Returns
    -------
    str
        The colored text"""
    return bcolors.CYAN + str(text) + bcolors.ENDC


def GREEN(text:Any) -> str:
    """Returns the text with the green color
    
    Parameters
    ----------
    text : Any
        The text to be colored
    
    Returns
    -------
    str
        The colored text"""
    return bcolors.GREEN + str(text) + bcolors.ENDC


def YELLOW(text:Any) -> str:
    """Returns the text with the yellow color
    
    Parameters
    ----------
    text : Any
        The text to be colored
    
    Returns
    -------
    str
        The colored text"""
    return bcolors.YELLOW + str(text) + bcolors.ENDC


def RED(text:Any) -> str:
    """Returns the text with the red color
    
    Parameters
    ----------
    text : Any
        The text to be colored
    
    Returns
    -------
    str
        The colored text"""
    return bcolors.RED + str(text) + bcolors.ENDC


def BOLD(text:Any) -> str:
    """Returns the text with the bold color
    
    Parameters
    ----------
    text : Any
        The text to be colored
    
    Returns
    -------
    str
        The colored text"""
    return bcolors.BOLD + str(text) + bcolors.ENDC


def UNDERLINE(text:Any) -> str:
    """Returns the text with the underline color
    
    Parameters
    ----------
    text : Any
        The text to be colored
    
    Returns
    -------
    str
        The colored text"""
    return bcolors.UNDERLINE + str(text) + bcolors.ENDC


if __name__ == "__main__":
    t = HEADER("HEADER ")
    t += BLUE("BLUE ")
    t += CYAN("CYAN ")
    t += GREEN("GREEN ")
    t += YELLOW("YELLOW ")
    t += RED("RED ")
    t += BOLD("BOLD ")
    t += UNDERLINE("UNDERLINE")

    print(t)