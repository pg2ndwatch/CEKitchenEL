import json
import boto3
import logging
import os
import sys
import traceback
from pathlib import Path


if Path(__file__).parent.parent not in sys.path:
    sys.path.append(Path(__file__).parent.parent)

if Path(__file__).parent not in sys.path:
    sys.path.append(Path(__file__).parent)


from Utilities import log_util as lu
from Utilities import parameter_util as pu
from Utilities import exception_util as eu

LAMBDA_NAME: str = 'ElTableParamVerifierLambda'

'''
Expected json string
{"table_name":"table_1",
 "table_schema_name":"dbo",
 "db_name":"database_name",
 "db_port":1433,
 "db_instance":"",
 "db_user":"pgadmin",
 "db_password":"1#peanuts",
 "db_max_retries":2,
 "row_count":12000,
 "column_list":["col1","col2,"col3","col4","col5"],
 "column_pk_list":["col1"],
 "data_type_list":["int","varchar","varchar","varchar","varchar"],
 "con_time_out_sec":"60",
 "log_level":"debug"
 }

'''



def RetrieveAllVerifiedParameters(p_event: dict) -> dict:

    l_return_verified_param_dict: dict = {}

    #-log_level-
    l_return_verified_param_dict['log_level'] = \
        pu.VerifyParameter(p_param_name='log_level',
                           p_params_dict=p_event,
                           p_default_value='WARNING',
                           p_valid_value_list=lu.LOG_LEVEL_OPTION_NAME_LIST)


    #-table_name-
    l_return_verified_param_dict['table_name'] = \
        pu.VerifyParameter(p_param_name='table_name',
                           p_params_dict=p_event,
                           p_default_value='')
    assert l_return_verified_param_dict['table_name'].param_found, 'parameter table_name not found!'

    assert (l_return_verified_param_dict['table_name'].param_value is not None) and \
           (len(l_return_verified_param_dict['table_name'].param_value) > 2), \
              f"Parameter 'table_name' has invalid value [{l_return_verified_param_dict['table_name'].param_value}]" \
              f" value must be at least 2 characters long!"


    #-db_name-
    l_return_verified_param_dict['db_name'] = \
        pu.VerifyParameter(p_param_name='db_name',
                           p_params_dict=p_event,
                           p_default_value='1433')
    assert l_return_verified_param_dict['db_name'].param_found,  'parameter db_name not found!'

    assert (l_return_verified_param_dict['db_name'].param_value is not None) and \
           (len(l_return_verified_param_dict['db_name'].param_value) > 2), \
              f"Parameter 'db_name' has invalid value [{l_return_verified_param_dict['db_name'].param_value}]" \
              f" value must be at least 3 characters long!"


    #-db_port-
    l_return_verified_param_dict['db_port'] = \
        pu.VerifyParameter(p_param_name='db_port',
                           p_params_dict=p_event,
                           p_default_value='1433')

    assert (l_return_verified_param_dict['db_port'].param_value is not None) and \
           (3 < len(l_return_verified_param_dict['db_port'].param_value) < 6), \
              f"Parameter 'db_port' has invalid value [{l_return_verified_param_dict['db_port'].param_value}]" \
              f" value must have 4 or 5 digits!"


    #-db_instance-
    l_return_verified_param_dict['db_instance'] = \
        pu.VerifyParameter(p_param_name='db_instance',
                           p_params_dict=p_event,
                           p_default_value='')

    assert (not l_return_verified_param_dict['db_instance'].param_found or
           len(l_return_verified_param_dict['db_instance'].param_value) > 2), \
        f"Parameter 'db_instance' has invalid value [{l_return_verified_param_dict['db_instance'].param_value}]" \
              f" value must be a length > 3 or be omitted!"


    # -db_user-
    l_return_verified_param_dict['db_user'] = \
        pu.VerifyParameter(p_param_name='db_user',
                           p_params_dict=p_event,
                           p_default_value='')
    assert l_return_verified_param_dict['db_user'].param_found,  'parameter db_user not found!'

    assert (l_return_verified_param_dict['db_user'].param_value is not None) and \
           (len(l_return_verified_param_dict['db_user'].param_value) > 1), \
              f"Parameter 'db_user' has invalid value " \
              f"[{l_return_verified_param_dict['db_user'].param_value}]" \
              f" value must be at least 2 characters long!"


    # -db_password-
    l_return_verified_param_dict['db_password'] = \
        pu.VerifyParameter(p_param_name='db_password',
                           p_params_dict=p_event,
                           p_default_value='')
    assert l_return_verified_param_dict['db_password'].param_found,  'parameter db_user not found!'

    assert (l_return_verified_param_dict['db_password'].param_value is not None) and \
           (len(l_return_verified_param_dict['db_password'].param_value) > 4), \
              f"Parameter 'db_password' has invalid value " \
              f"[{l_return_verified_param_dict['db_password'].param_value}]" \
              f" value must be at least 5 characters long!"


    # -db_max_retries-
    l_return_verified_param_dict['db_max_retries'] = \
        pu.VerifyParameter(p_param_name='db_max_retries',
                           p_params_dict=p_event,
                           p_default_value=0)

    assert (l_return_verified_param_dict['db_max_retries'].param_found or
           int(l_return_verified_param_dict['db_max_retries'].param_value) < 6), \
              f"Parameter 'db_max_retries' has invalid value " \
              f"[{l_return_verified_param_dict['db_max_retries'].param_value}]" \
              f" value must be less than 6 !"


    # -row_count-
    l_return_verified_param_dict['row_count'] = \
        pu.VerifyParameter(p_param_name='row_count',
                           p_params_dict=p_event,
                           p_default_value=0)

    assert (l_return_verified_param_dict['row_count'].param_found and
           int(l_return_verified_param_dict['row_count'].param_value) > 0), \
              f"Parameter 'row_count' has invalid value " \
              f"[{l_return_verified_param_dict['row_count'].param_value}]" \
              f" value must be > 0 !"


    # -column_list-
    l_return_verified_param_dict['column_list'] = \
        pu.VerifyParameter(p_param_name='column_list',
                           p_params_dict=p_event,
                           p_default_value='')

    assert l_return_verified_param_dict['column_list'].param_found,  'parameter column_list not found!'

    assert (l_return_verified_param_dict['column_list'].param_value is not []) and \
           (len(l_return_verified_param_dict['column_list'].param_value) > 0), \
              f"Parameter 'db_user' has invalid value " \
              f"[{l_return_verified_param_dict['column_list'].param_value}]" \
              f" value must have atlease one column in the list!"

    assert isinstance(l_return_verified_param_dict['column_list'].param_value[0], str), \
      f"Column name ({l_return_verified_param_dict['column_list'].param_value[0]}) is not a string!"

    assert len(l_return_verified_param_dict['column_list'].param_value[0]) > 0


    # -column_pk_list-
    l_return_verified_param_dict['column_pk_list'] = \
        pu.VerifyParameter(p_param_name='column_pk_list',
                           p_params_dict=p_event,
                           p_default_value=[])

    assert (not l_return_verified_param_dict['column_pk_list'].param_found or
          (l_return_verified_param_dict['column_pk_list'].param_value is not []) and \
           len(l_return_verified_param_dict['column_list'].param_value) > 0), \
              f"Parameter 'db_user' has invalid value " \
              f"[{l_return_verified_param_dict['column_pk_list'].param_value}]" \
              f" value must have at least one column in the list!"

    assert (not l_return_verified_param_dict['column_pk_list'].param_found or
            isinstance(l_return_verified_param_dict['column_pk_list'].param_value[0], str)), \
            f"Column name ({l_return_verified_param_dict['column_pk_list'].param_value[0]}) is not a string!"

    assert (not l_return_verified_param_dict['column_pk_list'].param_found or
            len(l_return_verified_param_dict['column_pk_list'].param_value[0]) > 0)


    # -data_type_list-
    l_return_verified_param_dict['data_type_list'] = \
        pu.VerifyParameter(p_param_name='data_type_list',
                           p_params_dict=p_event,
                           p_default_value='')

    assert l_return_verified_param_dict['data_type_list'].param_found,  \
        'parameter data_type_list not found!'

    assert (l_return_verified_param_dict['data_type_list'].param_value is not []) and \
           (len(l_return_verified_param_dict['data_type_list'].param_value) > 0), \
              f"Parameter 'db_user' has invalid value " \
              f"[{l_return_verified_param_dict['data_type_list'].param_value}]" \
              f" value must have atleast one column datatype in the list!"

    assert isinstance(l_return_verified_param_dict['data_type_list'].param_value[0], str), \
      f"Column name ({l_return_verified_param_dict['data_type_list'].param_value[0]}) is not a string!"

    assert len(l_return_verified_param_dict['data_type_list'].param_value[0]) > 0


    # -con_time_out_sec-
    l_return_verified_param_dict['con_time_out_sec'] = \
        pu.VerifyParameter(p_param_name='con_time_out_sec',
                           p_params_dict=p_event,
                           p_default_value=60)

    assert (not l_return_verified_param_dict['con_time_out_sec'].param_found or
           int(l_return_verified_param_dict['con_time_out_sec'].param_value) > 0), \
              f"Parameter 'con_time_out_sec' has invalid value " \
              f"[{l_return_verified_param_dict['con_time_out_sec'].param_value}]" \
              f" value must be > 0 !"


    return l_return_verified_param_dict



def lambda_handler(event, context):

    global LAMBDA_NAME
    status_code: int = -99999
    status_msg: str = "If this is returned, No Message Set by handler!"
    verified_parameter_dict: dict
    logger: logging = lu.GetDebugSession(p_session_name='__file__',
                                         p_log_level_name='WARNING')

    try:

        verified_parameter_dict = RetrieveAllVerifiedParameters(p_event=event)







        # Do work ###################
        logger.info(f" Lambda Function ({LAMBDA_NAME}) Executed!")

        #############################

        status_code = 200
        status_msg = 'OK'

    except AssertionError as ae:

        if logger is None:
            logging.basicConfig(level="DEBUG")
            logger = logging.getLogger(__file__)

        status_msg = f"An assertion error Occurred {ae.args[0]}) in lambda {LAMBDA_NAME}"
        status_code = 412

        logger.critical(status_msg)

    except Exception as e:


        if logger is None:
            logging.basicConfig(level="DEBUG")
            logger = logging.getLogger(__file__)

        status_msg = f"Unexpected Fatal error Occurred " \
                      f" in lambda {LAMBDA_NAME}. Trace [{eu.format_exception(e)}]"
        status_code = 500

        logger.fatal(status_msg)

    finally:

        return {'statusCode': status_code,
                'body': {'executed_lambda_with_name': LAMBDA_NAME,
                         'status_message': status_msg}}

