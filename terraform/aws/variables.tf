variable "instance_type" {
  description = "Tipo de instancia EC2"
  default     = "t2.micro"
}

variable "bucket_name" {
  description = "bucket_ejemplo_capa_raw"
}

variable "lambda_function_name" {
  description = "procesa_archivo_capa_raw_lambda"
}

variable "glue_job_name" {
  description = "procesa_archivo_capa_raw_gluejob"
}

variable "glue_job_name_pyspark" {
  description = "procesa_archivo_capa_raw_pyspark"
}
