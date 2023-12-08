import pyrebase
from secret import firebase_config

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()


def write(author:str, user:dict, data:dict):
    db.child("users").child(0).child(author).child("info").set(user)
    db.child("users").child(0).child(author).child("messages").push(data)
    return 

def fetch(user):
    return db.child("users").child(0).child(user).child("messages").get()
    

