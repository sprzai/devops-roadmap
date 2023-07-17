import logging

# Configuración básica de logging
logging.basicConfig(filename='example.log',         # Nombre de archivo para guardar los registros
                    level=logging.DEBUG,            # Nivel de registro mínimo para registrar
                    format='%(asctime)s:%(levelname)s:%(name)s: %(message)s',  # Formato del mensaje
                    filemode='w',                    # Modo de apertura de archivo ('w' sobrescribe, 'a' agrega)
                    datefmt='%Y-%m-%d %H:%M:%S')     # Formato de la fecha en el mensaje

# Registrar mensajes con diferentes niveles de severidad
logging.debug("Este es un mensaje de nivel DEBUG")
logging.info("Este es un mensaje de nivel INFO")
logging.warning("Este es un mensaje de nivel WARNING")
logging.error("Este es un mensaje de nivel ERROR")
logging.critical("Este es un mensaje de nivel CRITICAL")

# Crear un logger personalizado
logger = logging.getLogger("MiLoggerPersonalizado")

# Configurar el nivel de logging para este logger
logger.setLevel(logging.WARNING)

# Crear un manejador de archivo para el logger
file_handler = logging.FileHandler('mi_logger.log')
file_handler.setLevel(logging.WARNING)

# Crear un manejador de consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Definir un formato para los manejadores
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Agregar los manejadores al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Registrar mensajes con el logger personalizado
logger.debug("Este mensaje no se registrará, el nivel es demasiado bajo")
logger.warning("Este mensaje se registrará en el archivo pero no se mostrará en la consola")
logger.error("Este mensaje se registrará en el archivo y se mostrará en la consola")
