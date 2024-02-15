# Lutz 01Nov2023

import os

def rename_files():

    current_directory = os.getcwd()
    print("Renames files in ", current_directory)

    count = 0
    original_string = "original"
    new_string = "new"

    for filename in os.listdir(current_directory):
        new_filename = filename.replace(original_string, new_string)
        os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, new_filename))
     
        if original_string in filename:
            count = count + 1
    
    print(count, " ", original_string, " files counted")

if __name__ == "__main__":
  rename_files()