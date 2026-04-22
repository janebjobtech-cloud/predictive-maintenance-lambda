import json
import boto3
import uuid
import os

# AWS clients
s3 = boto3.client('s3')
runtime = boto3.client('sagemaker-runtime')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
def lambda_handler(event, context):
    print("EVENT RECEIVED:", json.dumps(event))

# Environment variables
TABLE_NAME = "PredictiveMaintenanceAlerts"
table = dynamodb.Table(TABLE_NAME)

ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']


def lambda_handler(event, context):
    try:
        # 1. Extract S3 bucket + object key from event
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # 2. Read the uploaded JSON payload from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        metric_payload = response['Body'].read().decode('utf-8')

        # 3. Invoke SageMaker endpoint
        sm_response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType='application/json',
            Body=metric_payload
        )

        prediction = json.loads(sm_response['Body'].read().decode('utf-8'))

        # 4. Create alert record
        alert_id = str(uuid.uuid4())
        alert_item = {
            "alert_id": alert_id,
            "s3_object": key,
            "prediction": prediction,
            "status": "ANALYZED"
        }

        # 5. Write alert to DynamoDB
        table.put_item(Item=alert_item)

        # 6. Publish alert to SNS
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="Predictive Maintenance Alert",
            Message=json.dumps({
                "alert_id": alert_id,
                "prediction": prediction,
                "s3_object": key
            })
        )

        # 7. Return success response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Inference completed and alert sent",
                "alert_id": alert_id,
                "prediction": prediction
            })
        }

    except Exception as e:
        # Return error response
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
