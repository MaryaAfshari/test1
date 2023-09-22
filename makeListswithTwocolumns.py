import os
import random

# Specify the path to the main dataset folder
dataset_folder = "../../../../mnt/disk1/data/DeepMine/wav"
#dataset_folder =  "/Users/maryamafshari/Desktop/Thesis_data/Deepmine Small Sample/SampleDeepMine/wav"

# Define split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create empty lists to store train, validation, and test lists
train_list = []
val_list = []
test_list = []

# Iterate over the speaker directories
for speaker_dir in os.listdir(dataset_folder):
    speaker_path = os.path.join(dataset_folder, speaker_dir)
    if not os.path.isdir(speaker_path):
        continue
    
    # Iterate over the session directories
    for session_dir in os.listdir(speaker_path):
        session_path = os.path.join(speaker_path, session_dir)
        if not os.path.isdir(session_path):
            continue
        
        # Iterate over the wave files in the session directory
        for filename in os.listdir(session_path):
            if filename.endswith(".wav"):
                # Extract the speaker ID, session ID, and file path
                speaker_id = speaker_dir
                session_id = session_dir
                file_path = os.path.join(session_path, filename)
                
                # Concatenate session_id and file_path using a delimiter
                file_path = os.path.join(session_id, filename)
                
                # Randomly assign the example to train, validation, or test list
                rand_value = random.random()
                if rand_value < train_ratio:
                    train_list.append((speaker_id, file_path))
                elif rand_value < train_ratio + val_ratio:
                    val_list.append((speaker_id, file_path))
                else:
                    test_list.append((speaker_id, file_path))

# Function to write a list to a file
def write_list_to_file(data_list, file_path):
    # Clear the contents of the file before writing
    open(file_path, "w").close()
    
    with open(file_path, "a") as file:
        for example in data_list:
            speaker_id, file_path = example
            file.write(f"{speaker_id} {file_path}\n")

# Write train list to a file, 2 Columns = v2
write_list_to_file(train_list, "train_list_v2.txt")

# Write validation list to a file, 2 Columns = 2 clmns
write_list_to_file(val_list, "val_list_v2.txt")

# Write test list to a file, 2 Columns = 2 clmns
write_list_to_file(test_list, "test_list_v2.txt")

print("Lists are ready. :) Thank GOD")