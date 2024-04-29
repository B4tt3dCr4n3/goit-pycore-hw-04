'''
Task 2. Write a function that reads a file and returns its content as a list of dictionaries.
'''
def get_cats_info(path: str) -> list[dict]:
    '''
    This function reads a file and returns its content as a list of dictionaries.
    '''
    try: # Check if the file exists
        with open(path, 'r', encoding='UTF-8') as file: # Open the file
            cats = file.readlines() # Read the file
            cats_info_new = [] # Initialize the list to store the cats information 
            for cat in cats: # Iterate through the cats
                cat = cat.strip().split(',') # Split the cat information
                cats_info_new.append({'id': cat[0], 'name': cat[1], 'age': cat[2]}) 
            return cats_info_new # Return the cats information
    except FileNotFoundError: # Catch the FileNotFoundError
        return 'File not found' # Return the error message
    
if __name__ == '__main__':
    FILE_PATH = '/Users/antonkorniyenko/VSCodeProjects/MSCbS/goit-pycore-hw-04/task_two/cats_file.txt'
    cats_info = get_cats_info(FILE_PATH)
    print(cats_info)

# def get_cats_info(path: str) -> list[dict]:
#     try:
#         with open(path, 'r') as file:
#             cats = file.readlines()
#             cats = [cat.strip().split(',') for cat in cats]
#             cats = [{'id': cat[0], 'name': cat[1], 'age': cat[2]} for cat in cats]
#         return cats
#     except FileNotFoundError:
#         return 'File not found'
    
# if __name__ == '__main__':
#     FILE_PATH = '/Users/antonkorniyenko/VSCodeProjects/MSCbS/goit-pycore-hw-04/task_two/cats_file.txt'
#     cats_info = get_cats_info(FILE_PATH)
#     print(cats_info)
