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

# open the json file to add/delete files
def open_json(value):
    # Get the current directory of the script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to "test.file"
    path = os.path.join(current_directory, '..', 'assets', 'known_faces.json')

    if value == 0:
        json_file = open(path, "w")
    elif value == 1:
        json_file = open(path, "a")
    else:
        json_file = open(path, "r")
    return path, json_file

# Define functions for each flag
def add_face(param):
    """
        add_face expects one element in param
        - the path of the image that will be added
        this function can only add one person's picture at a time so
        - no directory will be accepted as input
        - if the image has multiple faces it will only add
          the first detected face, so specify the name carefully
    """

    try:
        print("Adding face...")

        # check if path in the param exists
        if not os.path.exists(param):
            raise FileNotFoundError
        file = cv2.imread(param)
        
        # ask to enter the name
        face_name = None
        face_name = input("Enter name of the person:")
        if face_name == None:
            raise InvalidInputError("Please specify a name") 

        # detect face in the image
        face = detect_face(file)

        # find facial landmarks
        landmarks = face_landmarks(file, face)

        # encode the face
        encoded_face = np.array(face_encode(file, landmarks))
        encoded_face = encoded_face.tolist()

        print("Face encoded successfully")

        # open the json file
        path, json_file = open_json(1)

        # add the encoding in json
        data = {
            "Name": face_name,
            "Encoding": encoded_face[0]
        }

        # check if json file is empty
        if os.stat(path).st_size == 0:
            json_file.write("[\n")
        if os.stat(path).st_size == 2:
            with open(path, "ab") as json_truncate:
                json_truncate.seek(-1, 2)
                json_truncate.truncate()
                json_truncate.truncate()
        else:
            with open(path, "ab") as json_truncate:
                json_truncate.seek(-1, 2)
                json_truncate.truncate()
            json_file.write(",\n")

        # serialize face data in json file
        json.dump(data, json_file, indent=4, separators=(',', ':'))
        json_file.write("\n]")
        print("Face data added successfully.")
        print("Person recognized as: ", face_name)

        # close the file
        json_file.close()

    except FileNotFoundError as e:
        print(str(e))
        sys.exit(1)
    except InvalidInputError as e:
        print(str(e))
        sys.exit(1)

def delete_face(name):
    """
        delete_face expects one element in param
        - the exact name of the person whose data will be deleted

    """
    print("Deleting face", name,"...")

    path, json_fetch = open_json(2)
    if os.stat(path).st_size == 2:
        print("No faces to delete")
        return

    data = json.load(json_fetch)
    json_fetch.close()

    data = [item for item in data if item.get("Name") != name]

    path, json_del = open_json(0)
    json.dump(data, json_del, indent=4)
    print("Deleted face successfully")
    json_del.close()

# execute flag action
def execute_flag(flag, param):
    # Define flag-function mapping
    flag_actions = {
        '-a': add_face,
        '-d': delete_face
    }

    if flag in flag_actions:
        flag_actions[flag](param)
    elif flag == "-ad":
        raise InvalidFlagError("You can do one task at a time")
    elif flag == None:
        raise InvalidFlagError("Please enter a flag. -a to add faces, -d to delete faces")
    else:
        raise InvalidFlagError("Invalid Flag")

# Process the arguments
def process_arguments(arguments):
    for arg in arguments:
        if arg.startswith('-'):
            flag = arg
        else:
            param = arg

    return flag, param

def main(arguments):
    flag, param = process_arguments(arguments)
    execute_flag(flag, param)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    main(arguments)