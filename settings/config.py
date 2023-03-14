import boto3
from dotenv import dotenv_values

config = dotenv_values(".env")

# if True - user can see a traceback in terminal
# if False - user can see simple error message
debug_mode = False

access_key_id = config.get('ACCESS_KEY_ID')
secret_access_key = config.get('SECRET_ACCESS_KEY')

def connect_to_ec2():
    # connect to EC2 AWS
    return boto3.client('ec2', region_name='us-east-1', 
                        aws_access_key_id=access_key_id,
                        aws_secret_access_key=secret_access_key)

