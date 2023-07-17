## AWS CodeDeploy
## AWS CodeDeploy es un servicio de implementación completamente administrado
## que automatiza las implementaciones de software en diferentes servicios
## informáticos, como Amazon EC2, AWS Fargate, AWS Lambda y sus servidores
## locales
## Facilita el lanzamiento rápido de nuevas características, ayuda a evitar tiempos
## de inactividad durante la implementación de una aplicación y administra la
## compleja actualización de las aplicaciones
## Puedes usar CodeDeploy para automatizar implementaciones de software, lo que
## elimina la necesidad de realizar operaciones manuales propensas a errores
## EI servicio de CodeDeploy se adapta a sus necesidades de implementación

# Vamos a realizar un despliegue básico en una instancia EC2 utilizando AWS CodeDeploy:
# Instala AWS CLI:

# Si aún no tienes AWS CLI instalado, puedes instalarlo siguiendo las instrucciones proporcionadas en la página oficial de AWS CLI (https://aws.amazon.com/cli/).

# Configura AWS CLI:

# Después de instalar la CLI, necesitas configurarla con tus credenciales de AWS:
    $ aws configure

# Te pedirá que ingreses tu Access Key ID, Secret Access Key, región y formato de salida.

# Crea un archivo appspec.yml:

# AWS CodeDeploy necesita un archivo llamado appspec.yml en la raíz de tu repositorio. Este archivo le indica a CodeDeploy qué archivos desplegar y dónde
# , además de los scripts de ciclo de vida que debe ejecutar.

# Crea un bucket de S3 y sube tu aplicación:

# Crea un bucket de S3 para almacenar tu aplicación y luego sube tu código a ese bucket.    
    $ aws s3 mb s3://my-application-bucket
    $ aws s3 cp my-application.zip s3://my-application-bucket

# Crea una aplicación de CodeDeploy:
    $ aws deploy create-application --application-name my-application

# Crea un grupo de despliegue de CodeDeploy:
    $ aws deploy create-deployment-group --application-name my-application --deployment-group-name my-deployment-group --deployment-config-name CodeDeployDefault.OneAtATime --ec2-tag-filters Key=Name,Value=my-ec2-instance,Type=KEY_AND_VALUE --service-role-arn arn:aws:iam::your-account-id:role/CodeDeployServiceRole

# Crea un despliegue:
    $ aws deploy create-deployment --application-name my-application --deployment-config-name CodeDeployDefault.OneAtATime --deployment-group-name my-deployment-group --s3-location bucket=my-application-bucket,bundleType=zip,key=my-application.zip