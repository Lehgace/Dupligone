# Dupligone! ~ Prototype Duplicate Image Detection Application
Joshua Erickson | CPSC 491 Senior Project

## What is Dupligone?
Dupligone is a Python-based desktop application prototype. The end goal of Dupligone is to serve as an easily downloadable application that users can download to search for and remove duplicate photos from user supplied image directories. The application also aims to use a user friendly graphical interface for ease of use. The GUI chosen for the current implementation is CustomTkinter.

## How does the application work?
The general flow of the application guides the user through three main pages: the home page, file upload page, and search page.
* Home Page: Shows user the basic introduction on how to use the application

  ![homepageland](https://github.com/Lehgace/Dupligone/assets/122835808/ce8de09e-ccd5-43da-befe-862491f53982)
* Upload Page: Guides the user to upload the directories/images the user desires to check for duplicate images

  ![uploadpagepostbrowse](https://github.com/Lehgace/Dupligone/assets/122835808/d7b38fcd-9288-48e3-a019-97087f8b0565)
* Search Page: Runs the search algorithm, and shows display windows of all found duplicates. Contains simple editing and removal options.

  ![searchpageland](https://github.com/Lehgace/Dupligone/assets/122835808/75595bd6-4aaa-4c23-9daf-85b91ce5428b)

The search algorithm itself primarily uses the Python hashlib to assign each image found by the program a unique hash identification key based on the content of the image. As the program iterates through the uploaded directories, images with the same hash key are determined to be duplicates. The duplicates are then flagged and returned for usage in the search page for the user to manually review. 

The pages and general methods for the GUI are implemented in interface.py, while the search algorithm is implemented in search.py.

## What is the goal and inspiration of this project?
The goal of Dupligone is to create an easily downloadable software executable to improve the quality of life in managing the storage and importation of images. The program would have an easy to use interface that guides the user through the application. Additionally, the end vision is for the program to support the scalability of very large image directories as well as detection of near-duplicate images (images that are visually similar but not identical duplicates).   

The project is inspired from a problem I frequently encounter in uploading photos to my computer; having to manually scan through the imported folders and delete the duplicate images to save disk space. The aim of Dupligone is to perform this tedious process automatically, so that all the user has to do is manually comb over the duplicate images that Dupligone has already found for them. 

## Current Areas of Improvement and Limitations
Future improvements will include more functions as well as more fleshed out features and function integration. 

As it stands, the current Dupligone application acts as a prototype showcase of the endgame vision for said application. While most of the core features are present, they are mostly complete in the sense of demonstration purposes. Ideally, more development is necessary to fully flesh out the search algorithm as well as properly test functionality to scale with more expansive and diverse image directories. 

One big issue found in the application’s development was image compatibility for the chosen UI library of CustomTkinter. Future improvement would either plan on approaching the structure of the code to better integrate the functionality of CustomTkinter, or outright swapping to an alternative GUI environment where image functionality is more user friendly for development and scalability. The styling and intended functionality could also use further enhancement. Despite this, future improvements and approaches will serve to only further enhance the application to its original intended vision of being a powerful desktop application that can quickly find and delete the user’s duplicates; hassle free.
