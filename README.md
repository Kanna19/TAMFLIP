
# Initial Steps

Make sure you are in the root directory of the project (TAMFLIP) before proceeding.

## Create virtual environment
```
python3 -m venv pro_mode`
```

## Activate virtual environment
```
. pro_mode/bin/activate
```

Run `pip install --upgrade pip` if you want a newer version of pip.

## Install requirements
`pip install -r requirements.txt`

## Setting up the environment
```bash
export FLASK_APP=tamflip
export FLASK_ENV=development
``` 
To make sure evrything is running fine:
```
flask run
```

## Exit the virtual environment
`deactivate`

Note: Don't forget to activate the virtual environment everytime before you start developing and deactivate it after you are done.
