import os,sys
from pathlib import Path

if Path(__file__).parent.parent not in sys.path:
    sys.path.append(Path(__file__).parent.parent)

if Path(__file__).parent not in sys.path:
    sys.path.append(Path(__file__).parent)

from Utilities import log_util as lu
from Utilities import parameter_util as pu
from Utilities import exception_util as eu
import ElTableParamVerifier_lambda as el


def ContainerTest_handler(event, context):
    """Summary or Description of ContainerTest_handler()


    Parameters:
    event (dict): json parameters sent from caller. (see aws docs)
    context (dict) (not used): AWS Lambda context object. (see aws docs)

    Returns:
    dict: json serializable dict with test results for the container's stability.

   """





    LAMBDA_NAME:str = 'CEKitchen.ContainerTest_handler'

    return {'statusCode': 200,
            'body': {'executed_lambda_with_name': LAMBDA_NAME}}
