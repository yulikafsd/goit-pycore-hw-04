import sys

from faker import Faker
from pathlib import Path


fake = Faker("uk_UA")


def get_script_path(filename: str) -> Path:
    current_dir = Path(sys.argv[0]).resolve().parent
    return current_dir / filename


def generate_cats(filename: str) -> None:

    file_path = get_script_path(filename)

    if file_path.is_file():
        print("There is a file with such a name")
        return

    try:
        with open(file_path, "w", encoding="UTF-8") as file:
            for _ in range(10):
                fake_id = fake.uuid4().replace("-", "")
                fake_name = fake.first_name()
                fake_age = fake.random_int(min=1, max=20)
                print(f"{fake_id},{fake_name},{fake_age}")
                file.write(f"{fake_id},{fake_name},{fake_age}\n")

    except Exception as e:
        print(f"Something went wrong - {e}")

    print("File was created")


if __name__ == "__main__":
    generate_cats("cats.txt")
