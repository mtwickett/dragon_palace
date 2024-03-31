# Dragon Palace

This project uses Django to create a simple internal application for staff at a Chinese restaurant. Users can update drink entries using Django admin which are stored in a postgres database. The main feature of the app calculates the price of a drink from bottle attributes pulled from the database and pricing attributes inputted by the user.

## Set-Up

Create a folder for the project:
```
mkdir [folder_name]
```
Move into the folder and create a virtual environment:
```
python3 -m venv [.venv]
```
Activate the virtual environment:
```
source .venv/bin/activate
```
Upgrade pip:
```
python3 -m pip install --upgrade pip
```
Install Django:
```
python3 -m pip install Django
```
Check Django installation with:
```
django-admin --version
```
Clone the repo, then install requirements:
```
python3 -m pip install -r requirements.txt
```
Run the server locally:
```
python3 manage.py runserver
```
