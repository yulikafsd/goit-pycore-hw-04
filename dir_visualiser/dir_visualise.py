import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

I_CONNECTOR = "|  "
T_CONNECTOR = "├──"
CORNER_CONNECTOR = "└──"
DIR_ICON = "📁"
FILE_ICON = "📜"


def visualise_dir(path, prefix=""):

    if not path.exists():
        print(Fore.RED + f"There is no path: {path}")
        return

    if not path.is_dir():
        print(Fore.RED + f"{path} is not a directory")
        return

    if not prefix:
        print(f"{DIR_ICON} {Fore.CYAN}{path.name}")

    try:
        files = sorted(list(path.iterdir()))

    except PermissionError:
        print(Fore.RED + f"Access denied: {path}")
        return

    for index, file in enumerate(files):
        is_last = index == (len(files) - 1)
        connector = CORNER_CONNECTOR if is_last else T_CONNECTOR
        icon = DIR_ICON if file.is_dir() else FILE_ICON
        fore = Fore.CYAN if file.is_dir() else Fore.YELLOW
        print(f"{prefix}{connector}{icon} {fore}{file.name}")

        if file.is_dir():
            next_prefix = prefix + ("     " if is_last else I_CONNECTOR)
            visualise_dir(file, next_prefix)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Please enter command: python tree.py <directory_path>")
        sys.exit(1)

    directory = Path(sys.argv[1])
    visualise_dir(directory)
