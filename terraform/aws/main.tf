module "ec2" {
  source        = "./modules/ec2"
  instance_type = var.instance_type
}

module "s3" {
  source       = "./modules/s3"
  bucket_name  = var.bucket_name
}

module "lambda" {
  source               = "./modules/lambda"
  lambda_function_name = var.lambda_function_name
}

module "glue" {
  source                = "./modules/glue"
  glue_job_name         = var.glue_job_name
  glue_job_name_pyspark = var.glue_job_name_pyspark
}
