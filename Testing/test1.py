
from typing import Any
from FastDebugger import fd

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


class HEADER:
    """Returns the text with the header color

    Parameters
    ----------
    text : Any
        The text to be colored
    
    Returns
    -------
    str
        The colored text"""
    
    def __init__(self, text:Any) -> None:
        self.clean_text = text
        self.color_text = self._make_text_colored(text)

    def _make_text_colored(self, text:Any) -> str:
        return colors.HEADER + str(text) + colors.ENDC
    
    def add(self, other:Any) -> None:
        self.clean_text += other
        self.color_text = self._make_text_colored(self.clean_text)

    def __str__(self) -> str:
        return self.color_text
    
    def __repr__(self) -> str:
        return self.color_text
    
    def __len__(self) -> int:
        return len(self.clean_text)
    
    def __add__(self, other:Any) -> str:
        return self.clean_text + other
    
    def __mul__(self, other:int) -> str:
        return self.color_text * other
    
    def __rmul__(self, other:int) -> str:
        return other * self.color_text
    
    def __imul__(self, other:int) -> str:
        return self.color_text * other
    
    def __getitem__(self, key:Any) -> str:
        return self.clean_text[key]
    
    def __setitem__(self, key:Any, value:Any) -> str:
        self.clean_text[key] = value
        self._make_text_colored(self.clean_text)
        return self.color_text
    
    def __delitem__(self, key:Any) -> str:
        del self.clean_text[key]
        self._make_text_colored(self.clean_text)
        return self.color_text
    
    def __contains__(self, item:Any) -> bool:
        return item in self.clean_text
    
    def __iter__(self) -> str:
        return iter(self.clean_text)
    
    def __reversed__(self) -> str:
        return self.clean_text[::-1]
    
    def __eq__(self, other:Any) -> bool:
        return self.clean_text == other
    

    

    

    

    

if __name__ == '__main__':
    text = HEADER('Hello World!')

    u_text = text.add('!')

    print(text)
    print(u_text)

    # print(f'{text} is {len(text)} characters long')