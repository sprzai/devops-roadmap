resource "aws_s3_bucket" "b" {
  bucket = "bucket-name-layer-raw"
  acl    = "private"

  versioning {
    enabled = true
  }
}

resource "aws_s3_bucket_object" "object" {
  bucket = "bucket-name-layer-raw" # el mismo nombre del bucket creado arriba
  key    = "glue_script.py"
  source = "source/glue_script.py" # el camino a tu script local
  etag   = "${filemd5("source/glue_script.py")}"
}

resource "aws_s3_bucket_object" "object_pyspark" {
  bucket = "bucket-name-layer-raw" # el mismo nombre del bucket creado arriba
  key    = "glue_script_pyspark.py"
  source = "source/glue_script_pyspark.py" # el camino a tu script local
  etag   = "${filemd5("source/glue_script_pyspark.py")}"
}

