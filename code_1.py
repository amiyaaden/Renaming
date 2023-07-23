import os


def rename_images(folder_A, folder_B):
    for root, dirs, files in os.walk(folder_A):
        for dir_name in dirs:
            source_dir = os.path.join(root, dir_name)
            target_dir = os.path.join(folder_B, dir_name)
            names_file = os.path.join(target_dir, "names.txt")

            if not os.path.exists(names_file):
                print(f"Skipping {source_dir}. names.txt not found in {target_dir}")
                continue

            with open(names_file, "r") as file:
                names = file.read().splitlines()

            image_files = [
                file
                for file in os.listdir(source_dir)
                if os.path.isfile(os.path.join(source_dir, file))
            ]
            num_images = len(image_files)

            if len(names) < num_images:
                print(f"Skipping {source_dir}. Insufficient names in {names_file}")
                continue

            for i, image_file in enumerate(image_files):
                old_path = os.path.join(source_dir, image_file)
                new_name = names[i]
                new_name = new_name.lower().replace(" ", "-")
                new_path = os.path.join(
                    source_dir, new_name + os.path.splitext(image_file)[1]
                )
                os.rename(old_path, new_path)
                print(
                    f"Renamed {image_file} to {new_name + os.path.splitext(image_file)[1]}"
                )


# Example usage
folder_A = "location here"
folder_B = "location here"
rename_images(folder_A, folder_B)
