import sys
from pathlib import Path
import sys


# Create absolute path having relative
def get_absolute_file_path(relative_path: str) -> Path:
    script_directory = Path(sys.argv[0]).resolve().parent
    absolute_path = script_directory / relative_path
    return absolute_path


# Parse the file and calculate the salary
def total_salary(path: str):

    file_path_object = get_absolute_file_path(path)

    # Check if file exists and is file
    if not file_path_object.is_file():
        print(f"The path {path} doesn't lead to a file")
        return None

    total_sum = 0
    count = 0

    # Read the file and check the data in each line
    try:
        with open(file_path_object, "r", encoding="UTF-8") as file:
            for line in file:
                worker_data = line.strip().split(",")

                if len(worker_data) != 2:
                    print(f"Skip the line. Wrong format of line: {line.strip()}")
                    continue

                # Calculate total and average
                try:
                    salary = int(worker_data[1])
                    total_sum += salary
                    count += 1

                except ValueError:
                    print(
                        f"Skip the line. Salary is not an integer or a float: {line.strip()}"
                    )
                    continue

            if count == 0:
                print("No (salary) records found in file")
                return None

        average_salary = int(total_sum / count)
        return (total_sum, average_salary)

    except Exception as e:
        print(f"Ooops! {e}")
        return None


if __name__ == "__main__":

    result = total_salary("salaries.txt")

    # Check if result is not None and is unpackable
    if result:
        total, average = result
        print(f"Total salary: {total}, Average salary: {average}")
    else:
        print("Calculation failed or file not found. Cannot display results.")
