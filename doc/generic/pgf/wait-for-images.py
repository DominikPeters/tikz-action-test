import os
import glob
import time

# Directory to monitor
dir_path = 'pgfmanual-images'

def all_files_have_size(directory):
    # Get all svg and png files in the directory
    files = glob.glob(os.path.join(directory, '*.svg')) + glob.glob(os.path.join(directory, '*.png'))
    num_files = len(files)
    num_files_with_size_zero = 0
    # Check if all files have size > 0
    for file in files:
        if os.path.getsize(file) <= 0:
            num_files_with_size_zero += 1
    return num_files_with_size_zero, num_files

# Main loop
time_waited = 0
while time_waited < 700:
    num_files_with_size_zero, num_files = all_files_have_size(dir_path)
    if num_files_with_size_zero == 0:
        print("Finished - All SVG and PNG files have size greater than 0.")
        break
    else:
        print(f"{time_waited}s - Waiting - {num_files_with_size_zero}/{num_files} SVG and PNG files to have size greater than 0...")
        time.sleep(5)  # Wait for 5 seconds before checking again
        time_waited += 5
else:
    print("Timed out - Not all SVG and PNG files have size greater than 0.")
