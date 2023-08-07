# Usage
- Use the main script (Recommended)
  - run `run.sh`
    
    ```bash
        ./run.sh
    ```

    `run.sh` has 5 options: <br/>
    **(1)** Run Face Recognition <br/>
    **(2)** Add new face <br/>
    **(3)** See all listed faces <br/>
    **(4)** Delete a face <br/>
    **(5)** Exit <br/>

    Select what you wanna do

- Run Face Recognition manually using your webcam
  - run `FaceRecoMain.py`

    ```bash
        python FaceReco.py
    ```

- Add or delete a known face manually
  - run `faces.py`

    ```bash
        cd FaceRecoApi
        python faces.py -flag param
    ```

  - **faces.py** recognizes three types of flags
    - `-a` : add a face
      - `param` - to add a face you have to give the absolute path to the image
    - `-d` : delete a face
      - `param` - to delete a face you have to specify the exact name you added while adding the face in the param
    - `-l` : list all known faces
      - no `param`