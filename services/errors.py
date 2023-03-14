from botocore.exceptions import ClientError

from settings import config



def custom_error_handler(e:ClientError) -> None | SystemExit:
    """ Handle output for error depends on debug_mode """
    # Handle the exception
    if config.debug_mode:
        # Print the full traceback
        raise e
    else:
        # Print a custom error message
        print("[ERROR]: {}".format(str(e)))
        raise SystemExit(1)