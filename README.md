
# Initial Steps

## Create virtual environment
`python3 -m venv pro_mode`


## Activate virtual environment
(in the TAMFLIP folder (not tamflip))
`. pro_mode/bin/activate`

`pip install --upgrade pip` (if you want newer version of pip)

## Install requirements
`pip install -r requirements.txt`

## Exit the virtual environment
`deactivate`

Note: Don't forget to activate the virtual environment everytime before you start developing and deactivate it after you are done.


# Setting up the environment
```bash
export FLASK_APP=tamflip
export FLASK_ENV=development
``` 
To make sure evrything is running fine:
`flask run`
