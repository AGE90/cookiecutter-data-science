import subprocess

from colorama import just_fix_windows_console

just_fix_windows_console()

MESSAGE_COLOR = "\x1b[1;35m"
RESET_ALL = "\x1b[0m"

initialize_git_repository = "{{ cookiecutter.initialize_git_repository }}"

if(initialize_git_repository == 'yes'):
    print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")

    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}All set!{RESET_ALL}")