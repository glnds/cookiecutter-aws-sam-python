import boto3
import json
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
patch_all()

session = boto3.Session()


def lambda_handler(event, context):
    """
        AWS Lambda handler
        This method is invoked by the API Gateway: /Prod/first/{proxy+} endpoint.
    """
    message = get_message()

    return {
        "statusCode": 200,
        "body": json.dumps(message)
    }


@xray_recorder.capture('## get_message_segment')
def get_message():
    return {"hello": "world"}
