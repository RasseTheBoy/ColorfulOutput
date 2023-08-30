from FastDebugger import fd

from re import search


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

    START = '\033['
    END = 'm'

    ENDC = '\033[0m'


ANSI_color_range = [x for x in range (90, 97)]
ANSI_modif_range = [1,4]


class Base:
    """Base class for all ANSI colors."""
    ANSI_number:int
    ANSI_color:str
    
    def __new__(cls, text:str) -> str:
        """Color the text with the class's ANSI color.
        
        Parameters
        ----------
        text : str
            Text to add the color to
            
        Returns
        -------
        str
            The text with the color added
        """
        cls.ANSI_color = f'{ANSI.START}{cls.ANSI_number}{ANSI.END}'

        return cls._analyze_text(text)
    

    @classmethod
    def _get_values(cls, _t) -> list[int]:
        """Get values from an ANSI escape code
        
        Parameters
        ----------
        _t : str
            ANSI escape code
            
        Returns
        -------
        list[int]
            List of values from the ANSI escape code"""
        _t = _t.removeprefix(ANSI.START).split(ANSI.END)[0]
        if not _t:
            return []
        return [int(x) for x in _t.split(';')]
    

    @classmethod
    def _insert_number(cls, text:str, index:int=0) -> str:
        """Inserts the class's ANSI number in the text in the given index.
        
        Parameters
        ----------
        index : int
            Index of the start of the ANSI escape code
            
        Returns
        -------
        str
            The edited string with the added classe's number in the code
        """
        ansi_block_end_index = text.find('m')+1     # Find the end of the ANSI block to edit

        values = cls._get_values(text[:ansi_block_end_index]) # Get all values from the ANSI code block
        text_end = text[ansi_block_end_index:]      # Save the text that is after the ANSI block
        
        if cls.ANSI_number in ANSI_color_range:     # Iterate through all values in the ANSI code block
            values = [x for x in values if x not in ANSI_color_range] # Remove all other text coloring from values
        
        values.append(cls.ANSI_number)      # Append new ANSI number in the ANSI code block
        values = [str(x) for x in values]   # Convert all values to string

        ANSI_block = f'{ANSI.START}{";".join(values)}{ANSI.END}' # Build new ANSI block

        return f'{ANSI_block}{text_end}' # Return the edited ANSI block with the text after


    @classmethod
    def _analyze_text(cls, input_text:str) -> str:
        """Checks if the text contains any ANSI escape sequences.
        
        Combine sequences if the same types are written after each other.
        
        Parameters
        ----------
        input_text : str
            Text to analyze
            
        Returns
        -------
        str
            The text with the ANSI escape sequences combined
        """
        def remove_spaces(text:str) -> tuple[str, int, int]:
            """Removes empty spaces from a string.
            Returns the string, and how many spaces removed from the start and end.
            
            Parameters
            ----------
            text : str
                String to remove spaces from
                
            Returns
            -------
            tuple[str, int, int]
                The string, and how many spaces removed from the start and end"""
            text_len = len(text)
            return text.strip(), text_len - len(text.lstrip()), text_len - len(text.rstrip())


        def check_text_start(text:str):
            if text.startswith(ANSI.START):
                # Check if value is inside of '\033['
                if cls.ANSI_number in cls._get_values(text):
                    # print('String starts with given ANSI number')
                    return text
                
                # Add ANSI value inside '\033['
                return cls._insert_number(text)

            else: # Create new '\033['
                return f'{cls.ANSI_color}{text}'
            

        def check_text_end(text:str):
            # Check if text ends with ANSI.ENDC
            if text.endswith(ANSI.ENDC):
                return text
            
            # Add ANSI.ENDC if not found
            return text + ANSI.ENDC


        # Remove spaces from the start and end of the text
        stripped_text, start_spaces, end_spaces = remove_spaces(input_text)

        output_text = check_text_start(stripped_text)
        output_text = check_text_end(output_text)

        output_text = f'{start_spaces * " "}{output_text}{end_spaces * " "}'

        return output_text
    

class CYAN(Base):
    ANSI_number = 96

class PURPLE(Base):
    ANSI_number = 95

class BLUE(Base):
    ANSI_number = 94

class YELLOW(Base):
    ANSI_number = 93

class GREEN(Base):
    ANSI_number = 92

class RED(Base):
    ANSI_number = 91

class BLACK(Base):
    ANSI_number = 90


# print(f'{ANSI.RED}{ANSI.BOLD}Hello world! {ANSI.UNDERLINE}Here we are again!{ANSI.ENDC}')

t = f'{YELLOW("Hello ") + RED("world!")}'
t = BLACK(RED(t))

fd(t)
print(t)


# test = '\x1b[91;1;4mHello\x1b[0m world'

# _t = test.removeprefix('\x1b[').split('m')
# if not _t:
#     exit()

# _t = _t[0]
# fd(_t.split(';'))

# print(test)
# fd(test)