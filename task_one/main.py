"""
Task 1: Write the function that read the file and calculates the total and average salary.
"""

def total_salary(path: str) -> set:
    """
    This function calculates the total and average salary from a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        tuple: A tuple containing the total salary and the average salary.
    """
    try: # Checking if the file exists
        with open(path, 'r', encoding='UTF-8') as file: # Opening the file
            lines = file.readlines() # Reading the file
            total_salary = 0 # Initializing the total salary
            for line in lines: # Iterating through the lines
                salary = line.split(',')[1] # Getting the salary
                total_salary += float(salary) # Adding the salary to the total salary
            average_salary = total_salary / len(lines) # Calculating the average salary
        return total_salary, average_salary # Returning the total and average salary
    except FileNotFoundError: # Catching the FileNotFoundError
        return 'File not found' # Returning the error message

if __name__ == '__main__':
    FILE_PATH = '/Users/antonkorniyenko/VSCodeProjects/MSCbS/goit-pycore-hw-04/task_one/salary_file.txt'
    total, average = total_salary(FILE_PATH)
    print(f"Total salary: {total}, Average salary {average}")
