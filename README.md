
<pre align="center">
|\  _____\\   __  \|\   ____\|\  ___ \ |\   __  \|\  ___ \ |\   ____\|\   __  \    
\ \  \__/\ \  \|\  \ \  \___|\ \   __/|\ \  \|\  \ \   __/|\ \  \___|\ \  \|\  \   
 \ \   __\\ \   __  \ \  \    \ \  \_|/_\ \   _  _\ \  \_|/_\ \  \    \ \  \\\  \  
  \ \  \_| \ \  \ \  \ \  \____\ \  \_|\ \ \  \\  \\ \  \_|\ \ \  \____\ \  \\\  \ 
   \ \__\   \ \__\ \__\ \_______\ \_______\ \__\\ _\\ \_______\ \_______\ \_______\
    \|__|    \|__|\|__|\|_______|\|_______|\|__|\|__|\|_______|\|_______|\|_______|
</pre>

<br/>
<br/>

![FaceReco](https://socialify.git.ci/su1nta/FaceReco/image?description=1&font=Jost&forks=1&issues=1&language=1&name=1&pattern=Formal%20Invitation&pulls=1&stargazers=1&theme=Auto)

<h1 align="center">FaceReco is a funky name for Face Recognition</h1>

<h2>What it does</h2>

1. FaceReco can do three main things:
    - Facereco can detect faces shown in the camera or webcam in real-time
    - It recognizes known faces. You can add your face by simply adding an image which contains only your face recognize your face and write your specified name under your face
    - `WIP` If any unknown face is detected, it is e-mailed once in your specified email address

<h2>Tech and tools used</h2>

<h3>Languages and Libraries</h3>
<center>

|  |  |  |  |  |
| ------- | ------- | ------- | ------- | ------- |
| Python | OpenCV | Dlib | NumPy | JSON |

</center>
<h3>IDEs tested on</h3>
<center>

|       |       |
| ----- | ----- |
| Visual Studio Code | PyCharm |

</center>
<h3>OS tested on</h3>
<center>

|       |       |
| ----- | ----- |
|  ArchLinux | Windows 11 |
</center>

<h2>Installation</h2>

<h3>Linux</h3>

- Clone the repository
  - download the zip or
  - download in terminal

    ```bash
        git clone https://github.com/su1nta/FaceReco
    ```

- cd into the project directory

    ```bash
        cd FaceReco
    ```

- run `setup.sh`

    ```bash
        ./setup.sh
    ```

<h2>Usage</h2>

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

<h2>Configuration</h2>

Configuration is required only for developers

<h3>Add Environment variable in file cofiguration</h3>

**Note**: this config is required in every program where `dlib` or it's models are used

- PyCharm
  1. open the project
  2. open the file you want to configure to
  3. click on the three-dots on the top right of the file tabs
  4. click on Edit: a window should appear
  5. Under Environment Variables select the paste like icon > Click on `+` icon
  6. Set LD_LIBRARY_PATH= path/to/OpenBLAS (usr/local/lib in this case)
  7. Select Apply

- Visual Studio Code
  1. open/create a file named `Settings.json` inside .vscode directory
  2. inside the file add this object

    ```json
        {
            "python.env": {
            "LD_LIBRARY_PATH": "../venv/lib/"
            }
        }
    ```

  3. open `launch.json` inside .vscode directory
  4. add this key:value inside the `configurations` key

    ```json
        "env":{
                "LD_LIBRARY_PATH": "../venv/lib/"
            }
    ```
    
<h2>Documentation</h2>

Documentation can be found inside the `Docs` directory
