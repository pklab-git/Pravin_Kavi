import os
import shutil

# Function to read the file and process each line
def process_file_diff():
    added_path = "deployPackage/added"
    removed_path = "deployPackage/removed"

    # Ensure directories exist
    os.makedirs(added_path, exist_ok=True)
    os.makedirs(removed_path, exist_ok=True)

    with open('file_diff.txt', 'r') as file:
        with open('added.txt', 'w') as added_file:
            with open('removed.txt', 'w') as removed_file:
                for line in file:
                    status, path = line.strip().split(maxsplit=1)
                    filename = os.path.basename(path)
                    
                    if status in ['M', 'A']:  # Modified or Added
                        added_file.write(filename + '\n')
                        # Copy to added directory
                        shutil.copy(path, os.path.join(added_path, filename))
                    
                    elif status in ['R', 'D']:  # Renamed or Deleted
                        removed_file.write(filename + '\n')
                        # Move to removed directory
                        #shutil.move(path, os.path.join(removed_path, filename))    # Commented, instead using copy
                        # Copy to added directory
                        shutil.copy(path, os.path.join(removed_path, filename))


# Call the function to process the file
process_file_diff()

