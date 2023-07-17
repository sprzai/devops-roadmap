## pip install psutil

import psutil
import time

# Obtener la utilización de la CPU en porcentaje
cpu_percent = psutil.cpu_percent(interval=1)
print(f"Utilización de la CPU: {cpu_percent}%")

# Obtener la memoria física utilizada
mem = psutil.virtual_memory()
print(f"Memoria total: {mem.total} bytes")
print(f"Memoria usada: {mem.used} bytes")
print(f"Memoria disponible: {mem.available} bytes")
print(f"Porcentaje de memoria usada: {mem.percent}%")

# Obtener información sobre los discos
disk_partitions = psutil.disk_partitions()
print("Particiones de disco:")
for partition in disk_partitions:
    print(f"  {partition.device} - {partition.mountpoint} - {partition.fstype}")
disk_usage = psutil.disk_usage('/')
print(f"Uso del disco (raíz): {disk_usage.percent}%")

# Obtener información sobre la red
net_io = psutil.net_io_counters()
print(f"Bytes enviados: {net_io.bytes_sent}")
print(f"Bytes recibidos: {net_io.bytes_recv}")

# Listar todos los procesos en ejecución
print("Procesos en ejecución:")
for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(f"  PID {proc.info['pid']} - {proc.info['name']} - {proc.info['username']}")

# Obtener información sobre el proceso actual
current_process = psutil.Process()
print(f"Información del proceso actual: PID {current_process.pid}, Nombre {current_process.name()}")

# Monitorear la utilización de la CPU en tiempo real
print("Monitoreando la utilización de la CPU en tiempo real (detener con Ctrl+C):")
try:
    while True:
        print(f"Utilización de la CPU: {psutil.cpu_percent(interval=1)}%", end='\r')
except KeyboardInterrupt:
    print("\nMonitoreo detenido.")
