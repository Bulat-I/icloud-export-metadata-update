from datetime import datetime
import exiftool
import csv
import os

current_dir = os.getcwd()
photos_dir = current_dir + "/Photos"
if not os.path.exists(photos_dir):
    print("Photos directory not found. Please ensure that you execute the script from the right directory")

csv_files = []
for (root, dirs, file) in os.walk(photos_dir):
    for f in file:
        if '.csv' in f:
            csv_files.append(f)
            
if len(csv_files) == 0:
    print("CSV files with descriptions not found. Please ensure that you execute the script from the right directory")

for csv_file in csv_files:
    print("Current CSV file: " + csv_file)
    with open(os.path.join(photos_dir, csv_file)) as current_csv_file:
        reader = csv.reader(current_csv_file)
        for row in reader:
            image_file = os.path.join(photos_dir, row[0])
            filename = row[0]
            if filename == "imgName":
                continue
            if os.path.exists(image_file):
                with exiftool.ExifToolHelper() as et:
                    try:
                        date_str = str(row[5])
                        date_obj = datetime.strptime(date_str, '%A %B %d,%Y %I:%M %p %Z')
                        date_taken = (date_obj.strftime('%Y:%m:%d %H:%M:%S'))
                        
                        result = et.set_tags(
                            [image_file],
                            tags={
                                "DateTimeOriginal": date_taken,
                                "File:FileInodeChangeDate": date_taken,
                                "File:FileModifyDate": date_taken
                            },
                            params=["-P", "-overwrite_original"]
                        )
                        metadata = et.get_metadata(image_file)
                    except exiftool.exceptions.ExifToolException as e:
                        print("Failed to update metadata for the file: " + filename)
            else:
                print("File not found: " + filename)
