# Configuration
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