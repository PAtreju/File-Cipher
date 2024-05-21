# File-Cipher

File-Cipher is a Python-based application that allows users to encrypt and decrypt files using a generated key. The application also provides functionality to upload files to Google Drive.

## Requirements

- Python
- pip

## Python Modules

- tkinter
- cryptography.fernet
- googleapiclient.http
- google.auth.transport.requests
- google.oauth2.credentials
- google_auth_oauthlib.flow
- googleapiclient.discovery
- googleapiclient.errors

## Files in the Project

### `PythonCipher.py`

This file contains the `CipherFile` class which is responsible for encrypting and decrypting files. It also has a method to generate a key for encryption and decryption.

### `PythonGoogleAPI.py`

This file contains the `main` function which is responsible for uploading files to Google Drive. It uses the Google Drive API for this purpose.

### `PythonGUI.py`

This file contains the GUI for the application. It uses the tkinter library to create the GUI. The GUI allows users to select a key file, select a file to encrypt or decrypt, encrypt or decrypt the selected file, and upload the selected file to Google Drive.

### `PythonGUI.spec`

This file is used by PyInstaller to create an executable for the `PythonGUI.py` script. The executable can be run on systems without Python installed.

## How to Run
Go to dist folder and run the `PythonGUI.exe` or:



1. Install the required Python modules using pip:

```shellscript
pip install -r requirements.txt
```

2. Run the `PythonGUI.py` script:

```shellscript
python PythonGUI.py
```

3. Use the GUI to select a key file and a file to encrypt or decrypt. You can also create a new key file and upload files to Google Drive. Created key will apears in the same directory `dist`.

## Packaging with PyInstaller

The application can be packaged into a standalone executable using PyInstaller. The `PythonGUI.spec` file is used for this purpose. To create the executable, run the following command:

```shellscript
pyinstaller PythonGUI.spec
```

The executable will be created in the `dist` directory.

## Notes

- The application does not handle errors related to the absence or incorrect format of the `credentials.json` file for the Google Drive API, but will continue to run.
- The application does not handle errors related to the absence of the selected file or key file, but will continue to run.
- Remember to encrypt files before uploading them to Google Drive.