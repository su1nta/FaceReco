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
