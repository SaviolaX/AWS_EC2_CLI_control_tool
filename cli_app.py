import click, time

from rich.console import Console
from rich.live import Live

from services import tables, ec2_requests


# 'Rich' lib console instance to display pretty output
console = Console()


@click.group()
def cli() -> None:
    """ A tool for controlling instances """
    pass

@click.command(help='Show a list of all instances')
@click.option('-l', is_flag=True, default=False, 
              help='Display a table of instances in live mode.')
def list_instances(l:bool) -> None:
    """ Show a list of all instances """
    if l:
        req_count = 0

        with Live(tables.generate_table(), refresh_per_second=1) as live:
            print('\nTo STOP use CTR + C')
            # For endless cycle use: while True
            while req_count != 5: # send only 5 requests 
                time.sleep(5) # 5 sec pause between each requests to server
                live.update(tables.generate_table())
                req_count += 1
    else:
        table = tables.generate_table()
        console.print(table)
        

@click.command(help='Start an instance')
@click.option('-id', prompt='Enter instance ID', help='Start instance by ID')
def start_instance(id:str) -> None:
    """ Start instance by ID """
    start_response = ec2_requests.start_instance(instance_id=id)
    output_table = tables.start_instance_output(data=start_response)
    console.print(output_table)


@click.command(help='Stop an instance')
@click.option('-id', prompt='Enter instance ID', help='Stop instance by ID')
def stop_instance(id:str) -> None:
    """ Stop instance by ID """
    stop_response = ec2_requests.stop_instance(instance_id=id)
    output_table = tables.stop_instance_output(data=stop_response)
    console.print(output_table)
    

# initialize functions as commands
cli.add_command(list_instances)
cli.add_command(start_instance)
cli.add_command(stop_instance)


if __name__=='__main__':
    cli()