import os
import random
import shutil

# Paths
source_folder = r'D:\MURA-v1.1\total_nodes'
dest_folder1 = r'D:\MURA-v1.1\new_N1'
dest_folder2 = r'D:\MURA-v1.1\new_N2'
dest_folder3 = r'D:\MURA-v1.1\new_N3'

# Create destination folders if they don't exist
os.makedirs(dest_folder1, exist_ok=True)
os.makedirs(dest_folder2, exist_ok=True)
os.makedirs(dest_folder3, exist_ok=True)

# List all image files
images = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

# Shuffle the list
random.shuffle(images)

# Split into 3 parts
n = len(images)
split1 = n // 3
split2 = 2 * n // 3

part1 = images[:split1]
part2 = images[split1:split2]
part3 = images[split2:]

# Move files
for img in part1:
    shutil.move(os.path.join(source_folder, img), os.path.join(dest_folder1, img))

for img in part2:
    shutil.move(os.path.join(source_folder, img), os.path.join(dest_folder2, img))

for img in part3:
    shutil.move(os.path.join(source_folder, img), os.path.join(dest_folder3, img))

print("Images have been randomly divided into 3 folders!")
