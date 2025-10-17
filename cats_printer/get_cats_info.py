from pathlib import Path
import sys


# Create absolute path having relative
def get_absolute_file_path(relative_path: str) -> Path:
    script_directory = Path(sys.argv[0]).resolve().parent
    absolute_path = script_directory / relative_path
    return absolute_path


def get_cats_info(path: str):
    file_path_object = get_absolute_file_path(path)

    # Check if file exists and is file
    if not file_path_object.is_file():
        print(f"The path {path} doesn't lead to a file")
        return None

    cats_list = []
    count = 0

    # Read the file and check the data in each line
    try:
        with open(file_path_object, "r", encoding="UTF-8") as file:
            for line in file:
                cat_data = line.strip().split(",")

                if len(cat_data) != 3:
                    print(f"Skip the line. Wrong format of line: {line.strip()}")
                    continue

                id, name, age = cat_data
                cats_list.append({"id": id, "name": name, "age": age})
                count += 1

            if count == 0:
                print("No cat records found in file")
                return None

        return cats_list

    except Exception as e:
        print(f"Ooops! {e}")
        return None


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)
