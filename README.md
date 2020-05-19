
# Initial Steps

Make sure you are in the root directory of the project (TAMFLIP) before proceeding.

## Create virtual environment
```
python3 -m venv env
```

## Activate virtual environment
```
. env/bin/activate
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
## Credentials
The key value pairs for `EMAIL`, `APP_PASSWORD` and `SERVER_SECRET` should be specified in the file `credentials.txt`

Also the credentials for flight api have been deactivated. You can generate your own credentials [here](https://developers.amadeus.com/self-service/category/air) by registering an application (add these credentials in `api_module.py`).

## Exit the virtual environment
`deactivate`

Note: Don't forget to activate the virtual environment everytime before you start developing and deactivate it after you are done.
