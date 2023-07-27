from pyspark.context import SparkContext
from pyspark.sql import SparkSession, functions as F

sc = SparkContext()
spark = SparkSession(sc)

df = spark.read.csv("s3://input-bucket-name/input.csv")

df = df.withColumn('average', (df['column1'] + df['column2']) / 2)

df.write.csv("s3://landing-bucket-name/output.csv")
