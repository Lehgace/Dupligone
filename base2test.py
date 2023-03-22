# Joshua Erickson | CPSC 491 | Dupligone Base Algorithm 2 Test

import os # for managing folders and files
from tkinter import Tk 
from tkinter.filedialog import askdirectory # for GUI image prompt
from PIL import Image, ImageStat # Pillow Library for Image Detection (prototype 1)
import hashlib # for encoding unique hash ID's for scanned files

Tk().withdraw() # Do not display full GUI, avoid root directory 
path = askdirectory(title="Select base folder to search") # prompt user for base folder to search

walker = os.walk(path) # returns a tuple of main filepath, and its contents (subfolders, files)
uniqueImages = dict() # dictionary to contain unique image hash ID's (filehash, filepath)

for folder, sub_folder, files in walker:
    for file in files:
        filepath = os.path.join(folder,file)
        filehash = hashlib.md5(open(filepath, "rb").read()).hexdigest() #convert file into md5 hash-string, read bytes

        if filehash in uniqueImages:
            print(filepath, file)
            #os.remove(filepath) # immediately deletes found duplicate
            #print(f"{filepath} has been deleted")
            
        else:
            uniqueImages[filehash] = path
        
#print(uniqueImages)



# Original Base Test Results

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

print(f"Prototype 1 Duplicates: {duplicate_files}")
# To-Do: Integrate support with visual UI tool