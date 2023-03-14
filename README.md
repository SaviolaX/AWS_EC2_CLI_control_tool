## Instance controller

It is CLI tool in Python that can be used to control EC2 instances on AWS.

## Installation
- Clone repository on your machine: 
    - `git clone {current_repository_url}`
- Open repository: 
    - `cd ./CLI_TASK` 
- Create virtual environment: 
    - `python -m venv env`
- Install dependecies: 
    - `pip install -r requirements.txt`
- Create a new file `.env` and add there your AWS credentials. 
    - ``ACCESS_KEY_ID='your_key_id'``
    - ``SECRET_ACCESS_KEY='your_access_key'``

## Usage instruction
- To see all tool commands, type in console
    - `python cli_app.py` or `python cli_app.py --help`
- To see a list of all instances
    - `python cli_app.py list-instances`
- To see all instances in live, use flag `-l`. It opens all instances in live mode, to enter need to open second terminal window.
    - `python cli_app.py list-instances -l`
- To start instance
    - `python cli_app.py start-instance -id 'instance_id'`
- To stop instance
    - `python cli_app.py stop-instance -id 'instance_id'`

## Sample command lines
Input :
- `python cli_app.py` or `python cli_app.py --help`

Output example:

        Usage: cli_app.py [OPTIONS] COMMAND [ARGS]...

        A tool for controlling instances

        Options:
        --help  Show this message and exit.

        Commands:
        list-instances  Show a list of all instances
        start-instance  Start an instance
        stop-instance   Stop an instance

Input :
- `python cli_app.py list-instances`

Output example:

        
                    Instances
        ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┓
        ┃ ID                   ┃     CODE ┃       STATUS ┃
        ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━┩
        │ i-#################  │       01 │      running │
        │ i-#################  │       01 │      running │
        │ i-#################  │       00 │      stopped │
        └──────────────────────┴──────────┴──────────────┘

Input :
- `python cli_app.py list-instances -l`

Output example:

        
                    Instances
        ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┓
        ┃ ID                   ┃     CODE ┃       STATUS ┃
        ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━┩
        │ i-#################  │       01 │      running │
        │ i-#################  │       01 │      running │
        │ i-#################  │       00 │      stopped │
        └──────────────────────┴──────────┴──────────────┘

Input :
- `python cli_app.py start-instance -id i-#################`

Output example:

        
                     Starting instance
        ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┓
        ┃ ID                   ┃     CODE ┃       STATUS ┃
        ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━┩
        │ i-#################  │        0 │      pending │
        └──────────────────────┴──────────┴──────────────┘

Input :
- `python cli_app.py stop-instance -id i-#################`

Output example:

        
                     Stoping instance
        ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┓
        ┃ ID                   ┃     CODE ┃       STATUS ┃
        ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━┩
        │ i-#################  │        0 │     stopping │
        └──────────────────────┴──────────┴──────────────┘

## Error handling
Errors could be retreived:
- InvalidInstanceID - if added wrong instance id
    
        ==> python .\cli_app.py start-instance -id i-0224e66eafc2asdfs
        
        [ERROR]: An error occurred (InvalidInstanceID.Malformed) when calling the StartInstances operation: Invalid id: "i-0224e66eafc2asdfs"

- AuthFailure - if credentials are wrong (ACCESS_KEY_ID or SECRET_ACCESS_KEY)
    
        ==> python .\cli_app.py list-instances

        [ERROR]: An error occurred (AuthFailure) when calling the DescribeInstances operation: AWS was not able to validate the provided access credentials

- Error: No such command - if a command typed incorrect 
    
        ==> python .\cli_app.py list-instance

        Usage: cli_app.py [OPTIONS] COMMAND [ARGS]...
        Try 'cli_app.py --help' for help.

        Error: No such command 'wrong-command'.

## References
- AWS SDK for Python (Boto3) documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- AWS EC2 documentation: https://docs.aws.amazon.com/ec2/index.html
- Click library: https://click.palletsprojects.com/en/8.1.x/#documentation