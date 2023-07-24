#! /bin/bash

install_dependencies="pip install --no-cache-dir -r requirements.txt"

read -p "Enter name of the virtual enviornment to create : " dir

if [ -d "$dir" ]; then
    # echo "The directory '$dir' exists in the current folder."
    source "$dir"/bin/activate
    output=$(pip freeze)

    # Check if the output variable is empty or not
    if [ -z "$output" ]; then
        eval "$install_dependencies"
    else
        echo "Dependencies installed already"
    fi

else
    python -m venv "$dir"
    source venv/bin/activate
fi