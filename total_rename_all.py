# Lutz 01Nov2023

import os

def rename_files():

    new_filename = "new_filename"

    current_directory = os.getcwd()
    print("Renames files in ", current_directory)

    count = 0

    for filename in os.listdir(current_directory):
        
        source = filename  # Construct old file name
        # print("source: ", source)

        destination = new_filename + str(count) + ".png"
        # print("destination: ", destination)

        os.rename(source, destination)
     
        count = count + 1
    
    print(count, " ", " files counted")

if __name__ == "__main__":
  rename_files()