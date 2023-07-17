##  AWS CodeCommit
##  AWS CodeCommit es un servicio completamente administrado, de control de
##  código fuente, que aloja repositorios basados en Git.
##  AWS CodeCommit simplifica la colaboración en el código por parte de los
##  equipos, en un ecosistema seguro y con alta escalabilidad
##  Con CodeCommit no necesita utilizar su propio sistema de control de código
##  fuente ni preocuparse por el escalado de la infraestructura de dicho sistema.
##  CodeCommit funciona perfectamente con las herramientas de Git existentes
##  CodeCommit se puede utilizar para almacenar de forma segura cualquier
##  elemento, ya sea código fuente, archivos binarios, imágenes y scripts

Crear repositorio en AWS CodeCommit ( AWS -> CodeCommit )
    ingresar nombre de repositorio y descripcion
    agregar etiquetas: departamento : desarrollo


para conectarse al repositorio puede ser por hhtps o ssh
## conexion https
    ir a IAMS, buscar usuario en credenciales de seguridad, 
               generar clave https con usuario y clave.
    volvemos a codecommit y vamos a clonar repositorio -> copiamos url de descarga.
            git clone https://url_de_proyecto.git 
            antes de ejecutar el comando anterior se debe configurar la clave:
                    > aws configure -> AWS access key ID y clave [AWS Secret Access Key] generadas en IAM

se puede crear archivo desde la consola web.
confirmar los cambios.

################################################################
AWS CodeCommit es un servicio de control de versiones totalmente administrado que aloja repositorios Git seguros. Puedes usar CodeCommit para almacenar de manera segura cualquier cosa desde código fuente hasta binarios, y funciona de manera similar a otros sistemas de control de versiones.

A continuación, te proporciono un ejemplo simplificado de cómo se puede usar CodeCommit en un flujo de trabajo básico de DevOps.

Pasos	Instrucciones
Paso 1: Crear repositorio	Ve a la consola de AWS CodeCommit, selecciona "Crear repositorio" 
        y asigna un nombre a tu nuevo repositorio.
Paso 2: Configura tu entorno local	Necesitarás tener Git instalado en tu máquina. Además, debes 
        configurar las credenciales de AWS en tu máquina local para que puedas interactuar con el servicio CodeCommit.
Paso 3: Clonar el repositorio	Una vez que el repositorio esté creado y tu entorno local esté configurado, 
        puedes clonar el repositorio en tu máquina local con el comando git clone.
Paso 4: Realizar cambios	Realiza cambios en el código localmente en tu máquina. Estos cambios podrían ser 
        cualquier cosa, desde agregar nuevas características hasta corregir errores.
Paso 5: Commit y Push	Cuando estés satisfecho con los cambios, realiza un git commit para almacenar los cambios 
        en tu repositorio local. Luego, realiza un git push para enviar estos cambios al repositorio CodeCommit.
Paso 6: Revisión de código y merge	Otros miembros de tu equipo pueden ahora revisar tus cambios en el repositorio 
        de CodeCommit. Si los cambios son aceptados, pueden ser fusionados en la rama principal del código.
