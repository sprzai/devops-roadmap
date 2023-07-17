import os

# Obtener el directorio de trabajo actual
cwd = os.getcwd()
print(f"Directorio de trabajo actual: {cwd}")

# Cambiar el directorio de trabajo
os.chdir('/tmp')
print(f"Directorio de trabajo cambiado a: {os.getcwd()}")

# Listar archivos en el directorio actual
print("Archivos en el directorio actual:")
for file in os.listdir():
    print(file)

# Crear un nuevo directorio
os.mkdir('nuevo_directorio')
print("Nuevo directorio creado")

# Renombrar un archivo o directorio
os.rename('nuevo_directorio', 'directorio_renombrado')
print("Directorio renombrado")

# Crear subdirectorios
os.makedirs('directorio_renombrado/subdirectorio/subsubdirectorio')
print("Subdirectorios creados")

# Obtener variables de entorno
user = os.environ.get('USER')
print(f"Usuario del sistema: {user}")

# Ejecutar un comando del sistema
os.system('ls -la')
print("Comando del sistema ejecutado")

# Unir rutas
ruta_completa = os.path.join('/tmp', 'directorio_renombrado')
print(f"Ruta completa: {ruta_completa}")

# Volver al directorio de trabajo original
os.chdir(cwd)
print(f"Volvimos al directorio de trabajo original: {os.getcwd()}")
