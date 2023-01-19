import firebase_admin
from firebase_admin import firestore, credentials

class App:
    privateKey = credentials.Certificate("firebaseConf/messangercloud-firebase-adminsdk-d18ge-44966cb087.json")
    app = firebase_admin.initialize_app(privateKey)
    db = firestore.client()