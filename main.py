import csv

INPUT_FILE = "source_files/data.csv"

try:
    with open(INPUT_FILE, "r") as file:
        reader = csv.DictReader(file)

        print("Employees with Salary greater than 35000:\n")

        total_salary = 0
        count = 0

        for row in reader:
            salary = int(row["Salary"])

            if salary > 35000:
                print(
                    row["Name"],
                    row["Department"],
                    row["Salary"]
                )

                total_salary += salary
                count += 1

        if count > 0:
            average_salary = total_salary / count

            print("\nSummary")
            print("Total Employees:", count)
            print("Total Salary:", total_salary)
            print("Average Salary:", average_salary)

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")