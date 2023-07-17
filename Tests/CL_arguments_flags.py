import sys

# read command line arguments
arguments = sys.argv[1:]

flag = None
path = None

for arg in arguments:
    if arg.startswith('-'):
        flag = arg
    else:
        path = arg

if flag == '-a':
    print("You chose to add")
elif flag == '-b':
    print("You chose to delete")
elif flag == '-ab':
    print("You can't do both at same time!")
else:
    print("Invalid flag")

print("Your specified flag and path is:")
print("Flag: ", flag)
print("Path: ", path)
