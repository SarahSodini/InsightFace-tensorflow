import os
import shutil
import re

def organize_files(metadata_file, type):
    # Read metadata file
    # metadata = pd.read_csv(metadata_file)

    with open(metadata_file, "r") as file:
        data = file.readlines()

    for line in data:
        folder = re.search("\S+(?=/)", line)
        print(folder.group(0))
        folder = folder.group(0)
        image = re.search("(?<=/)\S+", line).group(0)
        destination_path = "..\data\DemogPairs\\" + type + "\\" + folder
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        shutil.copy2("..\data\DemogPairs\DemogPairs_112x112\\" + folder + "\\" + image, destination_path)
        os.rename(destination_path + "\\" + image, destination_path + "\\" + folder + "_" + image)
        
# Example usage:
type = 'test'
metadata_file = "..\data\DemogPairs\Metadata\Validate\Asian_Females_Validate.txt"
organize_files(metadata_file, type)
metadata_file = "..\data\DemogPairs\Metadata\Validate\Asian_Males_Validate.txt"
organize_files(metadata_file, type)
metadata_file = "..\data\DemogPairs\Metadata\Validate\Black_Females_Validate.txt"
organize_files(metadata_file, type)
metadata_file = "..\data\DemogPairs\Metadata\Validate\Black_Males_Validate.txt"
organize_files(metadata_file, type)
metadata_file = "..\data\DemogPairs\Metadata\Validate\White_Females_Validate.txt"
organize_files(metadata_file, type)
metadata_file = "..\data\DemogPairs\Metadata\Validate\White_Males_Validate.txt"
organize_files(metadata_file, type)
