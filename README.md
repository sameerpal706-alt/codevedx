# codevedx
# File Handling & Data Processing System

## Project Overview
This project demonstrates file handling and data processing using Python. It reads employee data from a CSV file, filters records based on salary, calculates summary statistics, and displays the processed results.

## Features
- Read data from CSV files.
- Handle file exceptions:
  - FileNotFoundError
  - PermissionError
- Filter employee records based on salary.
- Calculate summary statistics:
  - Total Employees
  - Total Salary
  - Average Salary
- Organized project structure for easy maintenance.
- Easy to modify file paths and configurations.

## Project Structure

```text
File Handling & Data Processing/
│
├── main.py
│
├── source_files/
│   └── data.csv
│
└── README.md
```

## Input File Format (`data.csv`)

```csv
ID,Name,Age,Department,Salary
1,Amit,22,IT,35000
2,Rahul,25,HR,30000
3,Priya,28,IT,45000
4,Sneha,24,Finance,40000
5,Vikas,30,IT,50000
```

## Technologies Used
- Python 3
- CSV Module

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/file-handling-data-processing.git
```

2. Navigate to the project folder:

```bash
cd file-handling-data-processing
```

3. Run the program:

```bash
python main.py
```

## Sample Output

```text
Employees with Salary greater than 35000:

Priya IT 45000
Sneha Finance 40000
Vikas IT 50000

Summary
Total Employees: 3
Total Salary: 135000
Average Salary: 45000.0
```

## Learning Outcomes
- File handling in Python
- CSV file processing
- Exception handling
- Data filtering and summarization
- Modular programming using functions

## Author
**Sameer Pal**
