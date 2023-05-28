import os
import re
import sys

from colorama import Fore, Style
from colorama import just_fix_windows_console

# Use Colorama to make Termcolor work on Windows too
just_fix_windows_console()

ERROR_COLOR = Fore.RED
MESSAGE_COLOR = Fore.CYAN
RESET_ALL = Style.RESET_ALL

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = "{{ cookiecutter.module_name }}"

if not re.match(MODULE_REGEX, module_name):
    print(ERROR_COLOR + "ERROR: {module_name=} is not a valid Python module name!" + RESET_ALL)
    print(MESSAGE_COLOR + "Please avoid using special characters" + RESET_ALL)
    sys.exit(1)
    
print(MESSAGE_COLOR + "Well done!" + RESET_ALL)
print(f"Creating project at { os.getcwd() }")