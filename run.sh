#! /bin/bash


# Decalring all global variables
run_loop=true
start_time=$(date +%s)      # Storing starting timestamp

ran_face_recognition=0
ran_add_face=0
ran_list_all_faces=0
ran_delete_face=0


# Calculate run time of the program
run_time() {
    end_time=$(date +%s)
    duration=$((end_time - start_time))

    if (( duration < 60 )); then
        echo "Script ran for $duration seconds."
    elif (( duration < 3600 )); then
        minutes=$(( duration / 60 ))
        seconds=$(( duration % 60 ))
        echo "Script ran for $minutes minutes and $seconds seconds."
    else
        hours=$(( duration / 3600 ))
        minutes=$(( (duration % 3600) / 60 ))
        seconds=$(( duration % 60 ))
        echo "Program ran for $hours hours, $minutes minutes, and $seconds seconds."
    fi
}

run_status()
{
    run_time
    echo "Ran face recogmition tests : $ran_face_recognition times"
    echo "Ran add face : $ran_add_face times"
    echo "Ran list all faces : $ran_list_all_faces times"
    echo "Ran delete face : $ran_delete_face times"
}
# Function to run face recognition
run_face_recognition() {
    ((ran_face_recognition += 1))
    echo_instructions
    echo "Running Face Recognition..."
    # python FaceRecoMain.py
    # Add your face recognition code here
}

# Function to add a new face
add_new_face() {
    ((ran_add_face += 1))
    echo_instructions
    echo "Adding New Face..."
    # Add your code to add a new face here
}

# Function to see all listed faces
see_all_faces() {
    ((ran_list_all_faces += 1))
    echo_instructions
    echo "Listing All Faces..."
    # Add your code to display all listed faces here
}

# Function to delete a face
delete_face() {
    ((ran_delete_face += 1))
    echo_instructions
    echo "Deleting a Face..."
    # Add your code to delete a face here
}

echo_instructions() {
    echo "Please select an option:"
    echo "1. Run Face Recognition"
    echo "2. Add new Face"
    echo "3. See All listed faces"
    echo "4. Delete a Face"
    echo "5. Exit"
    echo -e "\n\t"
}

# Main function to present the options and call corresponding functions
main() {
    
    clear
    echo_instructions
    read -p "Enter your choice (1-5): " choice

    case $choice in
        1)
            clear
            run_face_recognition
            ;;
        2)
            clear
            add_new_face
            ;;
        3)
            clear
            see_all_faces
            ;;
        4)
            clear
            delete_face
            ;;
        5)
            run_loop=false
            clear
            echo_instructions
            echo "Program terminated..."
            run_status
            ;;
        *)
            clear
            echo_instructions
            echo "Invalid choice. Please enter a number between 1 and 5."
            ;;
    esac
}

# Call the main function to start the program
while $run_loop
do
    main
done

