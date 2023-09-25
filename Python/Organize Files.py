import os
import shutil

folder_path = 'c:\\Users\\ezeki\\Desktop\\EPICS'  # Replace with the path to your folder

# Define the ranges for organizing files
file_ranges = [
    (1, 10),
    (11, 20),
    (21, 30),
    (31, 40),
    (41, 50)
]

# Create subfolders and move files
for start, end in file_ranges:
    subfolder_name = f'Ezekiel_{start:03d}_to_{end:03d}'
    subfolder_path = os.path.join(folder_path, subfolder_name)
    
    os.makedirs(subfolder_path, exist_ok=True)
    
    for i in range(start, end + 1):
        old_filename = f'Ezekiel_{i:03d}.jpg'  # Replace '.jpg' with the actual file extension
        new_filename = os.path.join(subfolder_path, old_filename)
        old_filepath = os.path.join(folder_path, old_filename)
        
        if os.path.exists(old_filepath):
            shutil.move(old_filepath, new_filename)
            print(f"Moved: {old_filename} -> {subfolder_name}")
        else:
            print(f"File not found: {old_filename}")

print("Organizing complete.")
