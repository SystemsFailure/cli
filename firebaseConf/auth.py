from firebase_admin import auth

def register(name: str, email:str, password:str):
    user = auth.create_user(
        email=email,
        password=password,
        display_name=name,
        disabled=False
    )
    print('2 proccess')
    print('user with email: {} been created successful'.format(user.uid))
