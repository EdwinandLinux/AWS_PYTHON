import boto3

ec2 = boto3.client('ec2', region_name='us-east-2')
# Run the instance
response = ec2.run_instances(
    ImageId='ami-0604f27d956d83a4d',  # Replace with a valid AMI ID
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='boto3'  #  Replace with a valid  key name
)
print(response)