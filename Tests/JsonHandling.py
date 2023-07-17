import os
import json

# data is stored in the json file as list of dictionaries

# take data as user input
data = {}

data["Name"] = input("Enter Name: ")
data["Course"] = input("Enter Course: ")
data["Sem"] = int(input("Enter Semester: "))
data["Roll"] = int(input("Enter Roll No: "))

# for key, value in data.items():
#     print(key,": ",value)

# dump/seralize a data in a json file

path = "Tests/json_data/test.json"

# open json file pointers
# fp(json file as append mode)
# fp_truncate(json file as append binary mode)
if os.path.exists(path):
    fp = open(path, "a")
    fp_truncate = open(path, "ab")
    print("file opened")
else:
    print(path+" doesn't exist")

# check if the file is empty
# this block is to manage the basic syntax of the json file
if os.stat(path).st_size == 0:
    print("File is empty. dumping...")
    fp.write("[\n")

else:
    print("File isn't empty. dumping...")
    fp_truncate.seek(-1, 2)
    fp_truncate.truncate()
    fp.write(",\n")

# write/serialize data in json file
json.dump(data, fp, indent=4, separators=(',', ':'))
fp.write("\n]")
print("Student data dumped to "+path)

# close opened files
fp.close()
fp_truncate.close()

# read/deserialize data from a json file
fp_read = open(path, "r")
# list of dictionaries
des_data = json.load(fp_read)
print("Student dataset read successfully")

# #print the deserialized data
for data in des_data:
    for key, value in data.items():
        print(key,": ",value)
