import botocore

from rich.table import Table
from rich.style import Style
from rich.text import Text

from settings import config
from . import ec2_requests

# connect to EC2 AWS
client = config.connect_to_ec2()


def create_table(table_title:str) -> Table:
    """ Create a table for output in console """
    table = Table(show_header=True, header_style="bold blue", title=f'\n{table_title}')
    table.add_column("ID", min_width=20)
    table.add_column("CODE", min_width=8, justify="right")
    table.add_column("STATUS", min_width=12, justify="right")
    return table


def status_color(status:str) -> str:
    """ Set cell background color depend on status """
    if status == 'pending':
        bg_color:str = Text(status, style=Style(bgcolor='yellow'))
    elif status == 'stopping':
        bg_color:str = Text(status, style=Style(bgcolor='indian_red'))
    elif status == 'stopped':
        bg_color:str = Text(status, style=Style(bgcolor='red'))
    elif status == 'running':
        bg_color:str = Text(status, style=Style(bgcolor='green'))
    return bg_color


def generate_table() -> Table:
    """ Create table and fill it up with instances data """
    
    # create table for instances
    table: Table = create_table(table_title='Instances')
    
    # information about: connection, instances ect
    desc_response: dict = ec2_requests.instances_information()
    
    # get instances
    instances: dict = desc_response['Reservations'][0]['Instances']
    # add instances in the table
    for instance in instances:
        table.add_row(
            str(instance['InstanceId']), 
            str(instance['State']['Code']),
            status_color(str(instance['State']['Name'])))
    return table

def start_instance_output(data:dict) -> Table:
    """ Create output for starting as table """
    instance_status:str = data['StartingInstances'][0]['CurrentState']['Name']
    instance_code:str = data['StartingInstances'][0]['CurrentState']['Code']
    instance_id:str = data['StartingInstances'][0]['InstanceId']
    
    table = create_table(table_title='Starting instance')
    table.add_row(
            str(instance_id), 
            str(instance_code),
            status_color(str(instance_status)))
    return table


def stop_instance_output(data:dict) -> Table:
    """ Create output for stopping as table """
    instance_status:str = data['StoppingInstances'][0]['CurrentState']['Name']
    instance_code:str = data['StoppingInstances'][0]['CurrentState']['Code']
    instance_id:str = data['StoppingInstances'][0]['InstanceId']
    
    table = create_table(table_title='Stopping instance')
    table.add_row(
            str(instance_id), 
            str(instance_code),
            status_color(str(instance_status)))
    return table