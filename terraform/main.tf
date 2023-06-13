// Módulo para crear una VPC en AWS
module "vpc" {
  source  = "./modules/vpc"      // Ubicación del código del módulo
  cidr_block = var.cidr_block    // Variable que define el bloque CIDR para la VPC
}

// Módulo para crear instancias EC2 en AWS
module "ec2" {
  source  = "./modules/ec2"      // Ubicación del código del módulo
  ami           = var.ami        // Variable que define la imagen de la máquina (AMI)
  instance_type = var.instance_type // Variable que define el tipo de instancia
  key_name      = var.key_name   // Variable que define el nombre de la clave SSH
  subnet_id     = module.vpc.subnet_id // Obtiene la ID de la subred creada por el módulo de la VPC
}

// Módulo para crear un balanceador de carga HTTP (ELB) en AWS
module "elb_http" {
  source  = "terraform-aws-modules/elb/aws" // Ubicación del código del módulo
  version = "~> 2.0"  // Versión del módulo

  name = "elb-example" // Nombre del balanceador de carga

  subnets         = module.vpc.subnet_ids // Usa las IDs de las subredes creadas por el módulo de la VPC
  security_groups = ["sg-12345678"] // Define los grupos de seguridad del ELB
  internal        = false // Define si el balanceador de carga es interno o no

  // Define los listeners para el balanceador de carga
  listener = [
    {
      instance_port     = 80  // Puerto en el que la instancia está escuchando
      instance_protocol = "HTTP" // Protocolo que la instancia está utilizando
      lb_port           = 80  // Puerto en el que el balanceador de carga está escuchando
      lb_protocol       = "HTTP" // Protocolo que el balanceador de carga está utilizando
    },
    {
      instance_port     = 8080
      instance_protocol = "http"
      lb_port           = 8080
      lb_protocol       = "http"
    },
  ]

  // Define el chequeo de salud para el balanceador de carga
  health_check = {
    target              = "HTTP:80/" // Objetivo del chequeo de salud
    interval            = 30 // Intervalo entre chequeos de salud
    healthy_threshold   = 2  // Número de chequeos exitosos para considerar la instancia como saludable
    unhealthy_threshold = 2  // Número de chequeos fallidos para considerar la instancia como no saludable
    timeout             = 5  // Tiempo de espera antes de considerar un chequeo de salud como fallido
  }

  // Define los registros de acceso para el balanceador de carga
  access_logs = {
    bucket = "my-access-logs-bucket" // Bucket S3 donde se almacenarán los registros de acceso
  }

  // Adjunta las instancias al balanceador de carga
  number_of_instances = 2 // Número de instancias que se adjuntarán
  instances           = module.ec2.instance_ids // IDs de las
