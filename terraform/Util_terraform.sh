## Este comando se usa para inicializar un directorio de trabajo que contiene archivos de configuración de Terraform. 
#,Este comando es seguro de ejecutar varias veces
#, para traer las configuraciones al estado más reciente.
terraform init

## Este comando crea un plan de ejecución. Terraform determina qué acciones 
# son necesarias para lograr el estado deseado especificado en los archivos de configuración.
terraform plan

## Este comando aplica los cambios necesarios para alcanzar el estado deseado de la configuración, 
# o el estado pre-determinado si no se proporciona ninguna configuración.
terraform apply

# Este comando destruye la infraestructura Terraform-managed.
terraform destroy

# Este comando valida los archivos de configuración en un directorio.
terraform validate

# Este comando se utiliza para reescribir los archivos de configuración a un formato de estilo canon.
terraform fmt

# Este comando se utiliza para administrar los espacios de trabajo. Los espacios de trabajo permiten tener múltiples estados en el mismo backend, 
# lo que puede ser útil para administrar entornos como staging, testing y production.
terraform workspace

# Este comando se utiliza para extraer el valor de una salida de un estado de Terraform.
terraform output

# Este comando se utiliza para actualizar el estado de Terraform con la infraestructura real.
terraform refresh

# Este comando se utiliza para importar la infraestructura existente en su estado de Terraform.
terraform import

# Este comando muestra la versión actual de Terraform que estás utilizando.
terraform version