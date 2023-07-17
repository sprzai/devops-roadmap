import subprocess

# Ejecutar un comando simple y obtener su salida
result = subprocess.run(['echo', 'Hola, Mundo!'], capture_output=True, text=True)
print(f"Salida del comando 'echo': {result.stdout}")

# Ejecutar un comando con múltiples argumentos
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(f"Salida del comando 'ls -l':\n{result.stdout}")

# Ejecutar un comando y capturar error en caso de fallo
try:
    result = subprocess.run(['ls', 'archivo_inexistente'], capture_output=True, text=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el comando 'ls archivo_inexistente': {e.stderr}")

# Ejecutar un comando y pasar datos a la entrada estándar
result = subprocess.run(['grep', 'python'], input='python es genial\njava es bueno', capture_output=True, text=True)
print(f"Salida del comando 'grep': {result.stdout}")

# Ejecutar un comando a través del shell (útil si el comando tiene tuberías, redirecciones, etc.)
result = subprocess.run('ls -l | grep py', capture_output=True, text=True, shell=True)
print(f"Salida del comando 'ls -l | grep py' usando el shell:\n{result.stdout}")

# Obtener el código de retorno de un comando
result = subprocess.run(['ls'])
print(f"Código de retorno del comando 'ls': {result.returncode}")
