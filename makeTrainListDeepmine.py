import os

def create_train_list(root_folder):
    train_list = []

    for dirpath, dirnames, filenames in os.walk(root_folder):
        if filenames:
            speaker_id = os.path.basename(dirpath)
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                train_list.append(f"{speaker_id} {file_path}")

    return train_list

# Example usage
root_folder = '/mylist'  # Replace with the root folder containing your files
train_list = create_train_list(root_folder)

# Print the train list
for item in train_list:
    print(item)