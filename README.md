# Script to recover metadata of photos exported from iCloud

Overview
========
If you ever decide to export all your iCloud photos using Apple's privacy.apple.com service, you may notice that all the timestamps of your media are gone, but the export comes with CSV files that contain all those timestamps for each file. 
This simple Python script will help you restore this metadata. The script reads timestamps from CSV files and uses the PyExifTool library to add them back to your media.

How to use
========
1. First, you need to request an export of your iCloud photo library through the privacy.apple.com service, then download those archives.
2. Normally, the iCloud export comes in a series of zip archives with the following structure:
<img width="248" alt="image" src="https://github.com/user-attachments/assets/60e52092-3f5a-4f45-8a02-d81d01a5e338">
<img width="271" alt="image" src="https://github.com/user-attachments/assets/e7d5da21-73b3-44ff-b6c7-49c5f8df30fe">
3. The main folder is Photos, which contains your media and CSV files. The other two folders may not exist, depending on your library.
4. To get the script to do its job, you need to clone this GitHub repo. Then install PyExifTool using the following command:
```
python3 -m pip install -r requirements.txt
```
5. Next, you need to place the restore_dates.py script next to your /Photos directory in each part of your export and run it.
6. The script finds all CSV files in your /Photos directory and goes through each line reading the timestamps. Since camera type, GPS geolocation and other metadata are usually already present, the script only restores timestamps using PyExifTool with the overwrite_original option enabled, which means that no copies of your files are made.
7. The script has been tested with typical iCloud content types: JPG, PNG, MOV, MP4, HEIC.
