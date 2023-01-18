import firebase_admin
from firebase_admin import firestore, credentials

privateKey = credentials.Certificate("firebaseConf/messangercloud-firebase-adminsdk-d18ge-44966cb087.json")
app = firebase_admin.initialize_app(privateKey)
db = firestore.client()

user = {
    'name': 'Lones',
    'email': 'Lones@gmail.com',
    'password': '31415Lones',
    'bio_info': 'none',
    'city': 'none',
    'countNotReadMessages': '0',
    'country': 'United States',
    'image_url': 'none',
    'lastMessageId': 0,
    'online': False,
    'status': 'none',
    'atCreated': 'none',
    'atUpdated': 'none',
    'arrayChats': [],
    'arrayConfigurations': [],
    'arrayFollowers': [],
    'arrayFollowing': [],
    'arrayMusicsFastAccess': [],
    'arrayMuteNotificationsUsers': [],
    'arrayNotReadMessages': [],
    'arrayPlaylists': [],
    'arrayСertainUsers': [],
}
def createNewUser():
    update_time, user_ref = db.collection('users').add(user)
    print('Added document with id {}'.format(user_ref.id))