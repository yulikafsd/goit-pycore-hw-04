import sys

from faker import Faker
from pathlib import Path


fake = Faker("uk_UA")


def get_script_path(filename) -> Path:
    current_dir = Path(sys.argv[0]).resolve().parent
    return current_dir / filename


def generate_salaries(filename: str) -> None:

    file_path = get_script_path(filename)

    if file_path.is_file():
        print("There is a file with such a name")
        return

    try:
        with open(file_path, "w", encoding="UTF-8") as file:
            for _ in range(10):
                fake_first = fake.first_name()
                fake_last = fake.last_name()
                fake_salary = fake.unique.random_int(min=1000, max=10000)
                file.write(f"{fake_first} {fake_last},{fake_salary}\n")
    except Exception as e:
        print(f"Something went wrong - {e}")
    
    print("File was created")


if __name__ == "__main__":
    generate_salaries("salaries.txt")
