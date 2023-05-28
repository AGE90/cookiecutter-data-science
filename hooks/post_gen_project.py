import subprocess

from colorama import Fore, Style
from colorama import just_fix_windows_console

# Use Colorama to make Termcolor work on Windows too
just_fix_windows_console()

MESSAGE_COLOR = Fore.CYAN
RESET_ALL = Style.RESET_ALL

initialize_git_repository = "{{ cookiecutter.initialize_git_repository }}"

if(initialize_git_repository == 'Yes'):
    print(MESSAGE_COLOR + "Initializing a git repository..." + RESET_ALL)

    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(MESSAGE_COLOR + "All set!" + RESET_ALL)