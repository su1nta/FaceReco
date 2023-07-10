# Bugs and Fixes

Bugs encountered throughout the project and their fixes are provided here

## Applicable on

- `IDE`: JetBrains PyCharm Community Edition
- `OS`: Arch Linux 6.1.33-1-lts
- `Python Interpreter`: python3.11

---

## cv2 error

### Errors

- ModuleNotFoundError: cv2 module not found

### Fix

- Install OpenCV manually on your venv (virtual environment)

  ```bash
    pip install opencv-python
  ```

---

## Dlib ImportError

There can be two types of ImportError found even after installing dlib

### Errors

- ImportError: undefined symbol:cblas_dtrsm
  - cblas is not installed by default sometimes
- ImportError: libopenblas.so.0:  cannot open shared object file: No such file or directory
  - this error occurs because the path to the library is not specified in the environment variables in the virtual environment

### Fix

- Clone OpenBLAS from their repo:

  ```bash
    git clone https://github.com/xianyi/OpenBLAS.git
  ```

- Enter in OpenBLAS directory and build it

  ```bash
    cd OpenBLAS
    make
  ```

- Install it in `/usr/local` (recommended) or any another preferred directory

  ```bash
    sudo make PREFIX=/path/to/installation install # /usr/local in this case
  ```

- Add Environment variable to the path where OpenBLAS is installed (usr/local in this case)
  - Open PyCharm > Triple dots on the upper right > Edit > Under Environment Variables select the paste like icon > Click on `+` icon
  - Set LD_LIBRARY_PATH= path/to/OpenBLAS (usr/local/lib in this case)
  - Select Apply
- Install cblas on your venv (virtual environment)

  ```bash
    sudo pacman -S cblas
  ```

- Reinstall dlib on your venv

  ```bash
    pip install --force-reinstall dlib
  ```

- Restart PyCharm

---

If you are still encountering the issue even after applying the fix, create an issue in this repo.

---

<br /><br />

## Import Error: site-packages/_dlib_pybind11.cpython-311-x86_64-linux-gnu.so: undefined symbol: dgeqrf\_

<br />

- `IDE`: IDE Independent
- `OS`: Arch Linux 6.1.33-1-lts
- `Python Interpreter`: python3.11

<br />

### It is still **unclear** why this error was occuring, but it seems to to be fixed for now.

<br />

## **Fix :**
  - Install below packages (Command applicable for archlinux)

<br />

  - ```
      sudo pacman -S cblas lapack
    ```

<br />

  - go into your project folder if not already there (***recomended to install system packages in another terminal windows to keep things clean and easy to work with***) 
  
  <br />

  - **Run :**
  
  
<br />

  - ```
      pip install --force-reinstall --no-cache-dir -r requirements.txt
    ```

    <br />
    - Above command will freshly download all requirements instead of using cached packages. (**this is recomended because just using --force-reinstall may result in installing cached packages**)
    
    <br />

  - reactivate venv (**not mandatory**)