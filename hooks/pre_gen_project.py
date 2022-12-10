import os
import re
import sys

from colorama import just_fix_windows_console

just_fix_windows_console()

ERROR_COLOR = "\x1b[0;31m"
MESSAGE_COLOR = "\x1b[1;36m"
RESET_ALL = "\x1b[0m"

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

project_slug = "{{ cookiecutter.project_slug }}"

if not re.match(MODULE_REGEX, project_slug):
    print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name. Please avoid using special characters{RESET_ALL}")
    sys.exit(1)
    
print(f"{MESSAGE_COLOR}Well done!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")