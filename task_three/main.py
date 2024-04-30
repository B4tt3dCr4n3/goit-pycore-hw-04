'''
Task 3: Write a Python program to visualize the directory structure of a specified directory.
'''

import sys
from pathlib import Path
from colorama import Fore

def visualize_directory_structure(directory: str = None, indent: str = '') -> None:
    '''
    This function visualizes the directory structure of a specified directory.

    Args: directory (str): The path to the directory. indent (str): /

    The indentation for output (used for recursion).
    '''
    if directory is None: # If no directory is provided, use the first command
        # line argument as the directory
        if len(sys.argv) > 1: # Check if there are any command line arguments
            directory = Path(sys.argv[1]) # Get the first command line argument as the directory
        else: # If no command line arguments are provided, print an error message
            print(
                Fore.RED +
                "No directory provided! Please provide directory as argument." +
                Fore.RESET) # Print error message
            print(
                Fore.WHITE +
                "USAGE: python3 main.py <directory>" + Fore.RESET) # Print usage information
            return directory # Return None if no directory is provided

    if directory is not None and directory.exists() and directory.is_dir(): # Check if
        # the directory exists and is a directory
        for item in directory.iterdir(): # Iterate over the items in the directory
            if item.is_dir(): # Check if the item is a directory
                print(f"{Fore.BLUE}{indent}{item.name}/{Fore.RESET}") # Print the
                # directory name with blue color
                visualize_directory_structure(item, indent + (' ' * len(item.name)))
                # Recursively visualize the subdirectory
            else: # If the item is a file
                print(f"{Fore.GREEN}{indent}{item.name}{Fore.RESET}") # Print the
                # file name with green color
    else: # If the directory does not exist or is not a directory
        print(Fore.RED + f"Directory \"{directory}\" does not exist!" + Fore.RESET) # Print
        # an error message

if __name__ == "__main__":
    visualize_directory_structure()

# '''
# Task 3: Write a Python program to visualize the directory structure of a specified directory.
# '''
# import sys
# from pathlib import Path
# from colorama import Fore

# def visualize_directory_structure(directory_path, indent=''):
#     '''
#     This function visualizes the directory structure of a specified directory.
#     '''
#     directory = Path(directory_path)
#     if directory.exists() and directory.is_dir():
#         for item in directory.iterdir():
#             if item.is_dir():
#                 print(f"{Fore.BLUE}{indent}{item.name}/{Fore.RESET}")
#                 visualize_directory_structure(item, indent + (' ' * len(item.name)))
#             else:
#                 print(f"{Fore.GREEN}{indent}{item.name}{Fore.RESET}")
#     else:
#         print(Fore.RED +
#               "The specified path does not exist or is not a directory!"
#               + Fore.RESET)

# def main():
#     '''
#     The main function of the program.
#     '''
#     if len(sys.argv) != 2:
#         print(Fore.RED +
#                 "Please specify the path to the directory as a command line argument!"
#                 + Fore.RESET)
#         print(Fore.WHITE +
#                 "USAGE: python3 main.py <directory>" + Fore.RESET)
#         return None

#     directory_path = sys.argv[1]
#     visualize_directory_structure(directory_path)

# if __name__ == "__main__":
#     main()
