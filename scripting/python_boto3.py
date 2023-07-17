
def get_client(service_name, region_name='us-west-2'):
    return boto3.client(service_name, region_name=region_name)

def list_s3_buckets():
    s3 = get_client('s3')
    return s3.list_buckets()

def list_lambda_functions():
    lambda_client = get_client('lambda')
    return lambda_client.list_functions()


def run_athena_query(query, database, output_location):
    athena = get_client('athena')
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database
        },
        ResultConfiguration={
            'OutputLocation': output_location
        }
    )
    return response

def start_execution(state_machine_arn, input):
    stepfunctions = get_client('stepfunctions')
    response = stepfunctions.start_execution(
        stateMachineArn=state_machine_arn,
        input=input
    )
    return response

def put_metric_data(namespace, metric_data):
    cloudwatch = get_client('cloudwatch')
    response = cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=metric_data
    )

def start_glue_job(job_name):
    glue = get_client('glue')
    response = glue.start_job_run(JobName=job_name)
    return response

def describe_clusters(cluster_identifier):
    redshift = get_client('redshift')
    response = redshift.describe_clusters(
        ClusterIdentifier=cluster_identifier
    )
    return response

def create_table(table_name, key_schema, attribute_definitions, provisioned_throughput):
    dynamodb = get_client('dynamodb')
    response = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput
    )
    return response

def main():
 
    # S3
    bucket_name = 'your-bucket-name'
    s3_service.create_bucket(bucket_name)
    s3_service.list_buckets()

    # Lambda
    function_name = 'your-lambda-function-name'
    lambda_service.invoke_lambda(function_name)

    # Athena
    query = "SELECT * FROM your_table;"
    database = "your_database"
    output_location = "s3://your-output-bucket/"
    athena_service.run_athena_query(query, database, output_location)

    # Glue
    job_name = "your-glue-job-name"
    glue_service.start_glue_job(job_name)

    # Step Functions
    state_machine_arn = 'your-state-machine-arn'
    input = '{}'
    step_functions_service.start_execution(state_machine_arn, input)

    # CloudWatch
    namespace = 'your-namespace'
    metric_data = [{
        'MetricName': 'your-metric',
        'Value': 123,
    }]
    cloudwatch_service.put_metric_data(namespace, metric_data)

    # Redshift
    cluster_identifier = 'your-cluster-identifier'
    redshift_service.describe_clusters(cluster_identifier)

    # DynamoDB
    table_name = 'your-table-name'
    key_schema = [{'AttributeName': 'your-key', 'KeyType': 'HASH'}]
    attribute_definitions = [{'AttributeName': 'your-key', 'AttributeType': 'S'}]
    provisioned_throughput = {'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
    dynamodb_service.create_table(table_name, key_schema, attribute_definitions, provisioned_throughput)

    print("All done!")
    
if __name__ == "__main__":
    main()