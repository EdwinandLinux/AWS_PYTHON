import boto3

ec2 = boto3.client('ec2', region_name='us-east-2')
response = ec2.terminate_instances(
    InstanceIds=[
        'i-067a08d328e202350',
    ]
)
