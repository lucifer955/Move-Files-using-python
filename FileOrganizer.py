#currently works only for pdfs                 

import glob,os
import shutil

#get the directory path  where the files resides 
src_path ='/home/lucifer955/Downloads/'

#get user input
file_type = input("Enter the file type here : ")

#select the file type  
arr = glob.glob(src_path + '*.%s' % file_type.lower())

#name of the new directory
directory  =  file_type.upper()+"s"

#get the path the new directory should be created
newPath = os.path.join(src_path,directory)

#folder is created here
os.mkdir(newPath)
print("Directory '% s' created" % directory)

#move all files to the created directory path
for file in arr :
    shutil.move(file,newPath)
