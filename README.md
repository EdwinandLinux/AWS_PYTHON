# 1 - Launch EC2 instance with Pyhton and BOTO3 Library
1 - Create a client
```
ec2= boto3.client('ec2' , region_name='us-east-2' )
```
2 - Run the  instance
```
response = ec2.run_instances(
    ImageId='ami-0604f27d956d83a4d',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='boto3' 
)
```