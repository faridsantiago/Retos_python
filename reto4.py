class AuthenticationError(Exception):
    pass

def user_auth(func):
    def wrapper(user, *args, **kwargs):
        if user['role'] == 'user':
            return func(user, *args, **kwargs)
        else:
            raise AuthenticationError("No tienes autorización para acceder a esta función.")
    return wrapper

def admin_auth(func):
    def wrapper(user, *args, **kwargs):
        if user['role'] == 'admin':
            return func(user, *args, **kwargs)
        else:
            raise AuthenticationError("No tienes autorización para acceder a esta función como administrador.")
    return wrapper

def superuser_auth(func):
    def wrapper(user, *args, **kwargs):
        if user['role'] == 'superuser':
            return func(user, *args, **kwargs)
        else:
            raise AuthenticationError("No tienes autorización para acceder a esta función como superusuario.")
    return wrapper

users_data = [
    {'username': 'user1', 'password': 'pass1', 'role': 'user'},
    {'username': 'admin1', 'password': 'pass2', 'role': 'admin'},
    {'username': 'superuser1', 'password': 'pass3', 'role': 'superuser'}
]

def login(username, password):
    for user in users_data:
        if user['username'] == username and user['password'] == password:
            return user
    return None

@user_auth
def user_function(user):
    return "Función para usuarios."

@admin_auth
def admin_function(user):
    return "Función para administradores."

@superuser_auth
def superuser_function(user):
    return "Función para superusuarios."

# Prueba de autenticación
username = input("Usuario: ")
password = input("Contraseña: ")
logged_user = login(username, password)

if logged_user:
    print("Bienvenido,", logged_user['username'])
    if logged_user['role'] == 'user':
        print(user_function(logged_user))
    elif logged_user['role'] == 'admin':
        print(admin_function(logged_user))
    elif logged_user['role'] == 'superuser':
        print(superuser_function(logged_user))
else:
    print("Credenciales inválidas.")
