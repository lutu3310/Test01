import firebase_admin  #sudo pip install firebase-admin
from firebase_admin import credentials

cred = credentials.Certificate("raspberrytest-86318-firebase-adminsdk-o41nj-f2c1199bf7.json")
firebase_admin.initialize_app(cred)