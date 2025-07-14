import os
import shutil

def collect_images(src_dirs, dest_dir, prefix):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    copied_files = 0
    skipped_files = 0
    file_tracker = {}  # Track filenames to check for duplicates

    for src_dir in src_dirs:
        for root, _, files in os.walk(src_dir):
            for file in files:
                if file.endswith('.png'):
                    path_parts = root.split(os.sep)

                    if len(path_parts) >= 3:
                        patient_id = path_parts[-2]  # Extract patient ID
                        study_folder = path_parts[-1]  # Extract study folder (e.g., study2_negative)

                        # Determine if the study is Negative or Positive
                        if 'negative' in study_folder.lower():
                            label = 'N'
                        elif 'positive' in study_folder.lower():
                            label = 'P'
                        else:
                            print(f" Skipping {root} - Could not determine label")
                            skipped_files += 1
                            continue

                        # Extract image number (e.g., image2.png → i2)
                        image_num = f"i{file.split('image')[-1].split('.')[0]}"

                        # Construct new filename
                        new_name = f"{prefix}_{patient_id}_{label}_{image_num}.png"

                        # Check for duplicate filenames
                        if new_name in file_tracker:
                            file_tracker[new_name] += 1
                            new_name = f"{prefix}_{patient_id}_{label}_{image_num}_{file_tracker[new_name]}.png"
                        else:
                            file_tracker[new_name] = 1

                        src_path = os.path.join(root, file)
                        dest_path = os.path.join(dest_dir, new_name)

                        try:
                            shutil.copy2(src_path, dest_path)
                            if os.path.exists(dest_path):  # Confirm copy success
                                copied_files += 1
                                print(f" Copied {src_path} → {dest_path}")
                            else:
                                print(f" Failed to copy {src_path}")
                        except Exception as e:
                            print(f" Error copying {src_path}: {e}")
                            skipped_files += 1
                    else:
                        print(f" Skipping {root} - Path does not have enough parts")
                        skipped_files += 1

    print("\n Transfer Summary:")
    print(f" Total copied files: {copied_files}")
    print(f" Total skipped files: {skipped_files}")

# Define source directories for N1
train_elbow_dir = 'MURA-v1.1/train/XR_ELBOW'
valid_elbow_dir = 'MURA-v1.1/valid/XR_ELBOW'
train_finger_dir = 'MURA-v1.1/train/XR_FINGER'
valid_finger_dir = 'MURA-v1.1/valid/XR_FINGER'

# Define source directories for N2
train_forearm_dir = 'MURA-v1.1/train/XR_FOREARM'
valid_forearm_dir = 'MURA-v1.1/valid/XR_FOREARM'
train_hand_dir = 'MURA-v1.1/train/XR_HAND'
valid_hand_dir = 'MURA-v1.1/valid/XR_HAND'

# Define source directories for N3
train_humerus_dir = 'MURA-v1.1/train/XR_HUMERUS'
valid_humerus_dir = 'MURA-v1.1/valid/XR_HUMERUS'
train_shoulder_dir = 'MURA-v1.1/train/XR_SHOULDER'
valid_shoulder_dir = 'MURA-v1.1/valid/XR_SHOULDER'
train_wrist_dir = 'MURA-v1.1/train/XR_WRIST'
valid_wrist_dir = 'MURA-v1.1/valid/XR_WRIST'


# Define destination directory for N1
destination_dir_1 = 'N1'

# Define destination directory for N2
destination_dir_2 = 'N2'

# Define destination directory for N3
destination_dir_3 = 'N3'

# creating files for N1
'''# Collect images for XR_Elbow (Prefix: EL)
collect_images([train_elbow_dir, valid_elbow_dir], destination_dir_1, 'EL')

# Collect images for XR_Finger (Prefix: FI)
collect_images([train_finger_dir, valid_finger_dir], destination_dir_1, 'FI')'''

# creating files for N2
'''# Collect images for XR_Elbow (Prefix: FO)
collect_images([train_forearm_dir, valid_forearm_dir], destination_dir_2, 'FO')

# Collect images for XR_Finger (Prefix: HA)
collect_images([train_hand_dir, valid_hand_dir], destination_dir_2, 'HA')
'''
# creating files for N3
# Collect images for XR_Elbow (Prefix: HU)
collect_images([train_humerus_dir, valid_humerus_dir], destination_dir_3, 'HU')

# Collect images for XR_Finger (Prefix: SH)
collect_images([train_shoulder_dir, valid_shoulder_dir], destination_dir_3, 'SH')

# Collect images for XR_Finger (Prefix: WR)
collect_images([train_wrist_dir, valid_wrist_dir], destination_dir_3, 'WR')