# import boto3

# S3Service=boto3.client("s3")

# CrBktCnf={'LocationConstraint': 'us-east-1'}

# S3Service.create_bucket(Bucket='bkt0405aryanjain')

import boto3

AWS_REGION="us-west-1"
S3Service=boto3.client("s3",region_name=AWS_REGION)

location={'LocationConstraint':AWS_REGION}

response=S3Service.create_bucket(Bucket='bkt0409aryanjain',CreateBucketConfiguration=location)
print("Response: ",response)