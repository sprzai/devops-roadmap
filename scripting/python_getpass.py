
import getpass

# Solicitar contraseña de forma segura
password = getpass.getpass("Ingresa tu contraseña: ")
print("Has ingresado tu contraseña de forma segura.")

# Solicitar usuario y contraseña
user = getpass.getuser()
password = getpass.getpass(f"Hola {user}, ingresa tu contraseña: ")
print("Has ingresado tu contraseña de forma segura.")

# Usar getpass para solicitar otra información sensible
secret_code = getpass.getpass("Ingresa tu código secreto: ")
print("Has ingresado tu código secreto de forma segura.")

# Usar getpass con un flujo de entrada personalizado
# (Esto es útil para pruebas o cuando la entrada proviene de una fuente diferente a la consola)
import io
fake_input = io.StringIO("mi_contraseña_falsa\n")
password = getpass.getpass("Ingresa tu contraseña: ", stream=fake_input)
print(f"Contraseña falsa ingresada: {password}")
