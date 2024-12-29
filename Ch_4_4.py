import glob

# Function to list files based on wildcard search
def make_file_list(directory, pattern):
    """
    Create a list of files matching a pattern in the specified directory.
    
    :param directory: Path to the directory to search.
    :param pattern: Wildcard pattern (e.g., '*.txt', '*.py').
    :return: List of matching file paths.
    
    search_path is created by concatenating the directory and pattern using the / delimiter.

    Example: If directory is "/home/user/documents" and pattern is "*.txt", the search_path would be "/home/user/documents/*.txt".

    """
    search_path = f"{directory}/{pattern}"
    file_list = glob.glob(search_path) #The glob.glob() function returns a list of file paths that match the search_path
    return file_list

# Example usage
directory = input("Enter the directory path: ")
pattern = input("Enter the wildcard pattern (e.g., *.txt, *.py): ")

# Generate and display the list of files
files = make_file_list(directory, pattern)
if files:
    print("\nFiles matching the pattern:")
    for file in files:
        print(file)
else:
    print("\nNo files found matching the pattern.")
