import os
import re

def extract_name_and_number(filename):

    pattern = r"\d+$"
    match = re.search(pattern, filename)
    
    name = filename[:len(filename)-len(match.group())]
    
    return name, match.group()


directory = input("Directory\nExample: /home/user/Desktop/source\nYour directory: ")
os.system(f"mkdir videos")

for root, _, files in os.walk(directory):

    files_jpg = []

    for file in files:
        if file.endswith('.jpg'): files_jpg.append(file)

    if len(files_jpg) > 0:
    
        files_jpg.sort()
        
        name, number = extract_name_and_number(files_jpg[0].split('.jpg')[0])
        
        path = root.replace("\\", "/")
        
        for filename in files_jpg[1:]:
        
            name_temp, number_temp = extract_name_and_number(filename.split('.jpg')[0])
            
            if name != name_temp or len(number) != len(number_temp):

                os.system(f"ffmpeg -framerate 24 -start_number {number} -i \"{path}\"/\"{name}%0{len(number)}d.jpg\" -pix_fmt yuv420p -c:v mjpeg videos/{name.replace(' ', '')}.mov")
                
                name = name_temp
                number = number_temp

        os.system(f"ffmpeg -framerate 24 -start_number {number} -i \"{path}/{name}%0{len(number)}d.jpg\" -pix_fmt yuv420p -c:v mjpeg videos/{name.replace(' ', '')}.mov")
