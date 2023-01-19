from firebase_admin import auth

def getUser(uid):
    user = auth.get_user(uid)
    return user


def register(name: str, email:str, password:str):
    user = auth.create_user(
        email=email,
        password=password,
        display_name=name,
        disabled=False
    )
    print('2 proccess')
    print('user with email: {} been created successful'.format(user.uid))


def update(uid, fields: dict):
    uid = getUser(uid)
    user = auth.update_user(
        uid,
        email=fields['email'],
        password=fields['password'],
        display_name=fields['name'],
        disabled=fields['mode']
    )
    return user