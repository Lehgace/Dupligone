# Joshua Erickson | CPSC 491 | Dupligone Base Algorithm 2 Test

import os # for managing folders and files
from tkinter import Tk 
from tkinter.filedialog import askdirectory # for GUI image prompt
from PIL import Image, ImageStat # Pillow Library for Image Detection (prototype 1)
import hashlib # for encoding unique hash ID's for scanned files

#Tk().withdraw() # Do not display full GUI, avoid root directory 

# Function that prompts user for working search directory
def browseFolder():
    path = askdirectory(title="Select base folder to search") # prompt user for base folder to search
    return path

# Function that returns walker iterator
def walkerFolder(path):
    walker = os.walk(path) # returns a tuple of main filepath, and its contents (subfolders, files)
    return walker

# Create empty dictionary to populate with duplicate files
uniqueImages = dict() # dictionary to contain unique image hash ID's (filehash, filepath)
# To-Do: Test to create empty dictionary to store filepath/files
foundFiles = dict()

# Test function to browse files and store filepaths uploaded
#uploaded_files = []
def uploadedFiles(uploaded_files):
    uploaded_files = os.listdir(browseFolder())
    #print(uploaded_files)
    return uploaded_files
#test = uploadedFiles()
#print(test)



# Function to find duplicates
# To-do thought: split function into two parts? one that returns full list of uploaded files w/ their hash keys. the other does actual duplicate comparison. 
def searchDuplicates(path, walker, uniqueImages):
    for folder, sub_folder, files in walker:
        for file in files:
            filepath = os.path.join(folder,file)
            filehash = hashlib.md5(open(filepath, "rb").read()).hexdigest() #convert file into md5 hash-string, read bytes

            if filehash in uniqueImages:
                # To-Do: Create variable to store filepath, file (name)
                #print(filepath, file)
                foundFiles[filehash] = (filepath, file)

                #os.remove(filepath) # immediately deletes found duplicate
                #print(f"{filepath} has been deleted")
                
            else:
                uniqueImages[filehash] = path
    
    return uniqueImages, foundFiles # returned list of duplicates, hash matches
            
#print(uniqueImages)

def interfaceSearch():
    path = browseFolder()
    walker = walkerFolder(path)
    imagesdict = dict()
    filepathsdict = dict() # for new feature

    # create the multiple return topuple decalartion here
    print(imagesdict)
    imagesdict, filepathsdict = searchDuplicates(path, walker, imagesdict)
    #print(imagesdict)
    return imagesdict, filepathsdict