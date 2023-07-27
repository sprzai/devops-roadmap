import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(database="database", table_name="table_name")
df = datasource0.toDF()

df = df.withColumn('average', (df['column1'] + df['column2']) / 2)

dynamic_frame_write = DynamicFrame.fromDF(df, glueContext, "dynamic_frame_write")
glueContext.write_dynamic_frame.from_options(frame=dynamic_frame_write, connection_type="s3", connection_options={"path": "s3://landing-bucket-name/output.csv"})
job.commit()
