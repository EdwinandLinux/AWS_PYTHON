# 1 - Launch EC2 instance with Pyhton and BOTO3 Library
1 - Create client
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

# 2 - Terminate EC2 instance with Python and BOTO3 Library

1 - Initialize EC2 client
```
ec2 = boto3.client('ec2', region_name='us-east-2')
```
2 - Terminate instance
```
response = ec2.terminate_instances(
    InstanceIds=[
        'i-067a08d328e202350',
    ]
)
```

# 3 - Launch EC2 instance and install Apache Server

1 - Create User data script to install Apache and create a simple webpage
```
user_data = '''
#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl enable -now httpd
sudo systemctl start httpd
echo "<h1> My Simple EC2 Website </h1>" | sudo tee  /var/www/html/index.html
```
```
2 - Create default VPC
```
ec2_client = boto3.client('ec2')
vpc = client.create_default_vpc()
vpc_id = vpc['Vpc']['VpcId']

```
3 - Create Security Group 
```
sg = ec2_client.create_security_group(
    GroupName ='sg_http',
    Description ='Alow HTTP access',
    VpcId = vpc_id
)
```
4 - Retrieve  security group ID
'''
sg_id = sg['GroupId']
'''
5 -  Add ingress rule to allow port 80
```
ec2_client.authorize_security_group_ingress(
    GroupId = sg_id,
    IpPermissions = [
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [ { 'CidrIp':'0.0.0.0' } ]
        }
    ]
)

```
6 - Lauch ec2 instance
```
ec2= boto3.client('ec2' , region_name='us-east-2' )
response = ec2.run_instances(
    ImageId='ami-0604f27d956d83a4d',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds = [sg_id],
    UserData=user_data,
    KeyName='boto3' 
    TagSpecifications = [
        {
            'ResourceType': 'instance' , 
            'Tags': [
                {
                    'key': 'ec2',
                    'Value': 'ec2_http'
                }
            ]
        }
    ]
)
```