# Joshua Erickson | CPSC 491 | Dupligone Base Algorithm Test

import os
from PIL import Image, ImageStat # Pillow Library for Image Detection

# Location of folder of images to search
#   To-Do: Integrate support for several folders 
image_folder = r'C:\Users\theun\OneDrive\Documents\Dupligone\TestImages'
# Scan through all files in the folder for images with .jpg and png extensions
#   To-Do: Integrate support for additional compatibale image extensions
image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpg') or _.endswith('png')]

# List to hold found duplicates
duplicate_files = []

# Begin search for duplicate images
for file_org in image_files:
    if not file_org in duplicate_files:
        image_org = Image.open(os.path.join(image_folder, file_org))
        pix_mean1 = ImageStat.Stat(image_org).mean

        for file_check in image_files:
            if file_check != file_org:
                image_check = Image.open(os.path.join(image_folder, file_check))
                pix_mean2 = ImageStat.Stat(image_check).mean

                if pix_mean1 == pix_mean2:
                    duplicate_files.append(file_org)
                    duplicate_files.append(file_check)

print(duplicate_files)
# To-Do: Integrate support with visual UI tool