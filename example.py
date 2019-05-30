import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIARVCBX5KOUZUGYMZX '
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'project-iot-v1'
FILE_NAME = 'test.txt';

data = open(FILE_NAME, 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data, ACL='public-read')

print ("Pushing to cloud")
