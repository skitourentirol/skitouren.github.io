import os
import shutil as s 

save_path = r'C:\VertiGIS\Uni\Webmapping\skitouren.github.io\data\Skitouren\Routen\GPX_Only'



for dictionary in os.listdir("Routen"):
    print(dictionary)
    path = os.path.join(r'C:\VertiGIS\Uni\Webmapping\skitouren.github.io\data\Skitouren\Routen', dictionary)
    print(path)
    for file in os.listdir(path):
        if file.endswith('.gpx'): 
            completePathSrc = os.path.join(path, file)
            completePathDst = os.path.join(save_path, file)

            s.copy2(completePathSrc, completePathDst)



         