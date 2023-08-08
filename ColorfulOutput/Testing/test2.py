
from FastDebugger import fd

from pprint import pprint

from typing import Any

class ANSI:
    CYAN = '\033[96'
    PURPLE = '\033[95'
    BLUE = '\033[94'
    YELLOW = '\033[93'
    GREEN = '\033[92'
    RED = '\033[91'
    BLACK = '\033[90'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    ENDC = '\033[0m'



class Base:
    ANSI_start = '\033['
    ANSI_color:str

    def __new__(cls, text:Any, bold:bool=False, underline:bool=False):
        def command_add(to_add):
            nonlocal command
            command += to_add

        def _check_text() -> Any:
            """Checks if the text contains any ANSI escape sequences.
            Combine sequences if the same types are written after each other.
            """
            nonlocal text

            

            if not isinstance(text, str):
                return text
            
            elif cls.ANSI_start not in text:
                return text
            
            else:
                pass
            
        _check_text()

        command = f'{cls.ANSI_start}{cls.ANSI_color}'
        if bold:
            command_add(';1')
        if underline:
            command_add(';4')

        command_add(f'm{text}{ANSI.ENDC}')
        return command
    



        




class RED(Base):
    ANSI_color = '91'

    def __new__(cls, text:Any, bold:bool=False, underline:bool=False) -> str:
        return super().__new__(cls, text, bold, underline)


if __name__ == '__main__':
    print(f'{RED(RED("Hello world!"), underline=True)!r}')

    # def color_text(text:Any, color:str) -> str:
    #     return color + str(text) + ANSI.ENDC

    # print(color_text('Hello World', ANSI.CYAN))