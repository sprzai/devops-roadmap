import platform

# Obtener el nombre del sistema operativo (e.g. 'Linux', 'Windows' o 'Darwin' para macOS)
os_name = platform.system()
print(f"Nombre del sistema operativo: {os_name}")

# Obtener la versión del sistema operativo
os_version = platform.release()
print(f"Versión del sistema operativo: {os_version}")

# Obtener la arquitectura de hardware
architecture = platform.architecture()
print(f"Arquitectura de hardware: {architecture}")

# Obtener información detallada de la plataforma
platform_info = platform.platform()
print(f"Información detallada de la plataforma: {platform_info}")

# Obtener el nombre de la máquina en la red
machine_name = platform.node()
print(f"Nombre de la máquina en la red: {machine_name}")

# Obtener información sobre el procesador
processor_info = platform.processor()
print(f"Información del procesador: {processor_info}")

# Obtener la versión de Python
python_version = platform.python_version()
print(f"Versión de Python: {python_version}")

# Obtener información detallada de la versión de Python
python_version_tuple = platform.python_version_tuple()
print(f"Información detallada de la versión de Python: {python_version_tuple}")

# Obtener la implementación de Python (e.g. 'CPython', 'PyPy')
python_implementation = platform.python_implementation()
print(f"Implementación de Python: {python_implementation}")

# Obtener la información del compilador de Python
python_compiler = platform.python_compiler()
print(f"Información del compilador de Python: {python_compiler}")
