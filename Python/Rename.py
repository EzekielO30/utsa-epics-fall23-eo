import os

folder_path = "c:\\Users\\ezeki\\Desktop\\epics"
new_name_prefix = 'Ezekiel_'
padding_width = 3  # Number of digits for padding (e.g., 001, 002, ...)

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Filter out non-image files (you can customize this if needed)
image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# Sort the image files for consistent numbering
image_files.sort()

# Count the total number of image files
total_images = len(image_files)

# Calculate the padding width needed based on the total number of images
padding_width = max(padding_width, len(str(total_images)))

# Iterate through the image files and rename them
for index, old_name in enumerate(image_files, start=1):
    extension = os.path.splitext(old_name)[1]  # Get the file extension
    new_number = str(index).zfill(padding_width)  # Add padding zeroes
    new_name = f"{new_name_prefix}{new_number}{extension}"
    
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    print(f"Renamed: {old_name} -> {new_name}")
    
print("Renaming complete.")
