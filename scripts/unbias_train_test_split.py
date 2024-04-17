import random

def split_metadata(metadata_file, validate_ratio=0.2):
    with open(metadata_file, "r") as file:
        data = file.readlines()
    
    # Om vi inte vill ha samma person i både träning och test; skippa shuffle och 
    # ändra splitten så den inte splittar på bilder av samma person
    random.seed(42)
    random.shuffle(data)
    
    # Calculate the number of lines for validation
    num_lines = len(data)
    num_val_lines = int(validate_ratio * num_lines)
    
    # Split into training and validation sets
    val_data = data[:num_val_lines]
    train_data = data[num_val_lines:]
    
    return train_data, val_data

def write_metadata(label, path):
	train_lines, val_lines = split_metadata(path)
	# Save the split datasets to separate files
	with open(f"../data/DemogPairs/Metadata/Train/{label}_Train.txt", "w") as train_file:
		train_file.writelines(train_lines)

	with open(f"../data/DemogPairs/Metadata/Validate/{label}_Validate.txt", "w") as val_file:
		val_file.writelines(val_lines)

write_metadata("Asian_Females", "../data/DemogPairs/Metadata/Original/Asian_Females.txt")
write_metadata("Asian_Males", "../data/DemogPairs/Metadata/Original/Asian_Males.txt")
write_metadata("Black_Females", "../data/DemogPairs/Metadata/Original/Black_Females.txt")
write_metadata("Black_Males", "../data/DemogPairs/Metadata/Original/Black_Males.txt")
write_metadata("White_Females", "../data/DemogPairs/Metadata/Original/White_Females.txt")
write_metadata("White_Males", "../data/DemogPairs/Metadata/Original/White_Males.txt")

print("Training metadata saved to train_metadata.txt")
print("Validation metadata saved to val_metadata.txt")