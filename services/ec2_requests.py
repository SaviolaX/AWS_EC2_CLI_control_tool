from botocore.exceptions import ClientError

from settings import config
from .errors import custom_error_handler


# connect to EC2 AWS
client = config.connect_to_ec2()


def instances_information() -> dict:
    """ Send request to AWS to get information about instances """
    try:
        res:dict = client.describe_instances()
        return res
    except ClientError as e:
        # Output error info depends on debug_mode
        custom_error_handler(e)
    

def start_instance(instance_id:str) -> dict:
    """ Start instance by ID """
    instance_id:list = [instance_id]
    try:
        return client.start_instances(
                    InstanceIds=instance_id
                )
    except ClientError as e:
        # Output error info depends on debug_mode
        custom_error_handler(e)


def stop_instance(instance_id:str) -> dict:
    """ Stop instance by ID """
    instance_id:list = [instance_id]
    try:
        return client.stop_instances(
                    InstanceIds=instance_id
                )
    except ClientError as e:
        # Output error info depends on debug_mode
        custom_error_handler(e)
        