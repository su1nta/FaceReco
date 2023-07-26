#! /bin/bash

install_dependencies="pip install --no-cache-dir -r requirements.txt"

read -p "Enter name of the virtual enviornment to create : " dir

if [ -d "$dir" ]; then
    echo "The directory named '$dir' exists in this current folder."

    sleep 1

    echo -e "Attempting to activate detected virtual enviornments...\n\n"
    
    source "$dir"/bin/activate

    output=$(pip freeze)

    # Check if the output variable is empty or not
    echo -e "Validating dependencies..."
    if [ -z "$output" ]; then
	sleep 1
	echo -e "Missing dependenciess\nInstalling Dependencies... \n\n"

	sleep 1
        
	eval $install_dependencies
    else
        echo -e "Dependencies already installed!\nQuitting now...\n\n"
    fi

else
    echo -e "Creating venv with name $dir\n\n"

    python -m venv "$dir"

    echo -e "Activating the venv\n\n"

    sleep 1
    
    source venv/bin/activate

    echo -e "Now installign required packages, please wait...\n\n"
    
    sleep 1
    
    eval $install_dependencies

    sleep 1

    echo ",,,Exiting,,,"
fi
