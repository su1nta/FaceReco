import sys
import os
import json
import cv2
import numpy as np
from api import detect_face, face_landmarks, face_encode

# InvalidFlagError - a custom exception
class InvalidFlagError(Exception):
    pass
class InvalidInputError(Exception):
    pass
class NoFaceFoundError(Exception):
    pass

# get the path to the known_faces.json
def get_json_path():
    # Get the current directory of the script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to "test.file"
    path = os.path.join(current_directory, '..', 
                        'assets', 'known_faces.json')

    return path

# list names in known_faces.json
def list_known_faces(_):
    path = get_json_path()

    with open(path, "r") as json_read:
        data = json.load(json_read)

    if len(data) == 0:
        raise NoFaceFoundError("No known faces")

    print("Known Faces are: ")
    list = [
        value for item in data 
        for key, value in item.items() if key == "Name"
        ]
    for name in list:
        print(name)

# Define functions for each flag

# add a face as known face
def add_face(param):
    """
        add_face expects one element in param
        - the path of the image that will be added
        this function can only add one person's picture at a time so
        - no directory will be accepted as input
        - if the image has multiple faces it will only add
          the first detected face, so specify the name carefully
    """

    print("Adding face...")

    # check if path in the param exists
    if not os.path.exists(param):
        raise FileNotFoundError
    file = cv2.imread(param)
        
    # ask to enter the name
    face_name = None
    face_name = input("Enter name of the person:")
    if not face_name.strip():
        raise InvalidInputError("Please specify a name") 

    # detect face in the image
    face = detect_face(file)

    # find facial landmarks
    landmarks = face_landmarks(file, face)

    # encode the face
    encoded_face = np.array(face_encode(file, landmarks))
    encoded_face = encoded_face.tolist()

    # if no face is detected, no face will be encoded
    if len(encoded_face) == 0:
        raise NoFaceFoundError("No face found")

    print("Face encoded successfully")

    # add the encoding in json
    data = {
        "Name": face_name,
        "Encoding": encoded_face[0]
    }

    # get file path of the json file
    path = get_json_path()

    # open json files
    json_append = open(path, "a")
    json_truncate = open(path, "ab")

    # check if json file is empty
    if os.stat(path).st_size == 0:
        json_append.write("[\n")
    if os.stat(path).st_size == 2:
        json_truncate.seek(-1, 2)
        json_truncate.truncate()
        json_truncate.truncate()
    else:
        json_truncate.seek(-1, 2)
        json_truncate.truncate()
        json_append.write(",\n")

    # serialize face data in json file
    json.dump(data, json_append, indent=4, separators=(',', ':'))
    json_append.write("\n]")
    print("Face data added successfully.")
    print("Person recognized as: ", face_name)

    # close json files
    json_append.close()
    json_truncate.close()


# delete a known face
def delete_face(name):
    """
        delete_face expects one element in param
        - the exact name of the person whose data will be deleted

    """

    print("Deleting face", name,"...")

    # get file path of the json file
    path = get_json_path()

    if os.stat(path).st_size == 2:
        print("No faces to delete")
        return

    with open(path, "r") as json_read:
        data = json.load(json_read)

    new_data = [item for item in data if item.get("Name") != name]
    if new_data == data:
        raise NoFaceFoundError("No face found named", name)

    with open(path, "w") as json_write:
        json.dump(new_data, json_write, indent=4)
        print("Deleted face successfully")

# execute flag action
def execute_flag(flag, param):
    # Define flag-function mapping
    flag_actions = {
        '-a': add_face,
        '-d': delete_face,
        '-l': list_known_faces
    }

    if flag in flag_actions:
        flag_actions[flag](param)
    elif flag == "-ad":
        raise InvalidFlagError("You can do one task at a time")
    elif flag == None:
        raise InvalidFlagError(
            "Please enter a flag: -a to add faces, -d to delete faces"
            )
    else:
        raise InvalidFlagError("Invalid Flag")

# Process the arguments - separate the flag and specified path/name
def process_arguments(arguments):
    for arg in arguments:
        if arg.startswith('-'):
            flag = arg
        else:
            param = arg

    # if just list the known faces no parameter is required
    if flag == '-l':
        param = " "

    return flag, param

def main(arguments):
    try:
        flag = None 
        param = None
        flag, param = process_arguments(arguments)
        execute_flag(flag, param)
    except InvalidFlagError as e:
        print(str(e))
    except FileNotFoundError as e:
        print(str(e))
    except InvalidInputError as e:
        print(str(e))
    except NoFaceFoundError as e:
        print(str(e))
    

if __name__ == "__main__":
    arguments = sys.argv[1:]
    main(arguments)