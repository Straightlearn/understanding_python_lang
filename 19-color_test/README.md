# To color text

## using colorama module

There are many built-in modules and libraries that in Python to which we can use to print the colored text.
Colorama is one of these built-in Python modules which can help to display the text in different colors. 
It is used to make the code more readable. 

Three formatting options are available in this module for coloring text. These are Back, Fore and Style. 
'Back' for background, 'For' is for foreground color and 'Style' for text test style.

available colors are

GREEN
BLUE
WHITE
YELLOW
MAGENTA
CYAN
WHITE

available styles

DIM
NORMAL
BRIGHT

## Python colorama init() function

we use the init() function to initialize colorama before using it in our program or script. the init() can be used with or without arguement. There are special keywords used , if want to use arguement.

### Autoreset (arguement)
    Autoreset, is used to reset the color and style after each line when the value of this argument is set to True.
i.e colorama.init(autoreset=True)
### Strip (arguement)
    Strip is used to remove the ANSI code from the output when the value of this argument is set to True.

### Convert (arguement)
    It is used to convert the ANSI code of the output when the value of this argument is set to True.
### Wrap (arguement)
    It is used to disable the overriding task when the value of this argument is set to False.
