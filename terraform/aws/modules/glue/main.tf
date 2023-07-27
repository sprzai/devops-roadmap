resource "aws_glue_catalog_database" "default" {
  name = "default"
}

resource "aws_iam_role" "glue_service_role" {
  name = "AWSGlueServiceRole"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_glue_job" "glue_job" {
  name     = var.glue_job_name
  role_arn = aws_iam_role.glue_service_role.arn

  command {
    script_location = "s3://${var.bucket_name}/glue-script.py"
    python_version  = "3"
  }
}

resource "aws_glue_job" "glue_job_pyspark" {
  name     = var.glue_job_name_pyspark
  role_arn = aws_iam_role.glue_service_role.arn

  command {
    script_location = "s3://${var.bucket_name}/glue-script-pyspark.py"
    python_version  = "3"
    name            = "glueetl"
  }
}
