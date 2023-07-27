import boto3
import pandas as pd
from io import StringIO

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'input-bucket-name'
    file_key = 'input.csv'
    landing_bucket_name = 'landing-bucket-name'
    landing_file_key = 'output.csv'
    
    csv_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')

    df = pd.read_csv(StringIO(csv_string))
    df['average'] = df.mean(axis=1)

    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(landing_bucket_name, landing_file_key).put(Body=csv_buffer.getvalue())
