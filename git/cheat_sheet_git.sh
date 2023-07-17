# !/bin/bash

# Inicializa un nuevo repositorio Git en el directorio actual
git init

# Clona (copia) un repositorio Git remoto a tu máquina local
git clone <url_del_repositorio>

# Muestra el estado de tu repositorio Git (cambios sin seguimiento, cambios listos para confirmar, etc.)
git status

# Agrega todos los cambios actuales al área de preparación para la próxima confirmación
git add .

# Agrega un archivo específico al área de preparación para la próxima confirmación
git add <nombre_del_archivo>

# Confirma los cambios agregados con un mensaje descriptivo
git commit -m "Mensaje descriptivo de los cambios"

# Muestra el historial de confirmaciones en el repositorio
git log

# Cambia a una rama diferente en tu repositorio
git checkout <nombre_de_la_rama>

# Crea una nueva rama en tu repositorio y cambia a ella
git checkout -b <nombre_de_la_nueva_rama>

# Fusiona los cambios de una rama diferente a tu rama actual
git merge <nombre_de_la_rama>

# Muestra las diferencias entre tu rama actual y otra rama
git diff <nombre_de_la_rama>

# Actualiza tu repositorio local con los cambios del repositorio remoto
git pull

# Envía tus cambios locales al repositorio remoto
git push

# Muestra las ramas existentes en tu repositorio local
git branch

# Elimina una rama local en tu repositorio
git branch -d <nombre_de_la_rama>

# Muestra la configuración de tu repositorio Git
git config --list

# Establece el nombre del usuario para tu repositorio Git
git config --global user.name "Tu Nombre"

# Establece el correo electrónico del usuario para tu repositorio Git
git config --global user.email tu@correo.com

# Deshace el último commit
git reset --hard HEAD~1

# Muestra cambios entre la confirmación de HEAD y la confirmación anterior
git show

