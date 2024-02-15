# Lutz 01Nov2023

import os

def rename_files():
    count = 0
    new_filename = "new_filename"
    filetype = ".png"
    current_directory = os.getcwd()
    print("Renaming files in ", current_directory)

    for file in os.listdir(current_directory):
        split_tup = os.path.splitext(str(file)) # 0 - name, 1 = ext
        # print("split_tup", split_tup)

        if split_tup[1] == filetype :

            print("filename: ", file)

            new_file = new_filename + str(count) + filetype
            print("new_file: ", new_file)

            os.rename(file, new_file)
        
            count = count + 1
        # endif split_tup
    # endfor file
            
    print(count, " ", " files counted")

if __name__ == "__main__":
  rename_files()
