import os
from PIL import Image

def resize_images(input_folder, output_folder, target_size):
    os.makedirs(output_folder, exist_ok=True)
    
    # Traverse through the directory structure
    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith(('.jpg')):
                with Image.open(os.path.join(root, filename)) as img:
                    img_resized = img.resize(target_size)
                    
                    # Determine output folder structure
                    relative_path = os.path.relpath(root, input_folder)
                    output_subfolder = os.path.join(output_folder, relative_path)
                    
                    # Create output subfolder if it doesn't exist
                    os.makedirs(output_subfolder, exist_ok=True)
                    
                    # Save the resized image to the output subfolder
                    output_path = os.path.join(output_subfolder, filename)
                    img_resized.save(output_path)
                    print(f"Resized {os.path.join(root, filename)} and saved as {output_path}")

input_folder = "../data/DemogPairs/DemogPairs_250x250"
output_folder = "../data/DemogPairs/DemogPairs_180x180"
target_size = (180, 180)

resize_images(input_folder, output_folder, target_size)