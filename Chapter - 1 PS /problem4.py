import os

# Specify the directory you want to list
directory_path = '.'  # '.' refers to the current directory

try:
    # Get the list of all files and directories
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
