from firebaseConf.firebaseApp import App

app = App()
db = app.db

user = {
    'name': 'NickBro',
    'email': 'NickBro@gmail.com',
    'password': '31415NickBro',
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
    update_time, user_ref =  db.collection('users').add(user)
    doc = user_ref.get()
    if doc.exists:
        print(doc.to_dict())
        return doc.to_dict()
    print('1 proccess')
    print('Added document with id {}'.format(user_ref.id))