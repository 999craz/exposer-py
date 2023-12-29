# Exposer

Simple Discord Bot made in Python. Made for personal use.

## Features

- Stores deleted messages in a Firebase Realtime DB.  
- Get user's deleted messages by mention.  

## Getting started  

### Create a secrets.py file containing your firebase_config, discord bot token and your discord uid.  

### With python virtual env  

`python -m venv venv`  
Using powershell: `venv\Scripts\activate.ps1`  
Using cmd: `venv\Scripts\activate.bat`  
`pip install -r requirements.txt`  

### With docker  

`docker build -t exposer .`  
`docker run --name exposer exposer`  
