import logging

'''
expected_parameters = \
        {'table_name': 'STR',
         'table_schema_name': 'STR',
         'db_name': 'STR',
         'db_port': 'int',
         'db_instance': 'str',
         'db_user': 'STR',
         'db_password': 'STR',
         'db_max_retries': 'int',
         'row_count': 'int',

         'column_list': 'list[STR]',
         'column_pk_list': 'list[STR]',`
         'data_type_list': 'list[STR],float|FLOAT|int|INT',

         'con_time_out_sec': 'int',
         'log_level': 'str,DEBUG|debug|INFO|info|WARN|warn|WARNING|warning|ERROR|error|CRITICAL|critical|FATAL|fatal'}
'''


def verify(p_parameter_type: tuple,
           p_logger: logging,
           p_param_value=None):

    p_param_value_sent_type = type(p_param_value)

    param_key_name: str = p_parameter_type[0]
    param_val_expected_type: str = p_parameter_type[1]
    param_val_expected_list_of_values: [] = []


    if ',' in param_val_expected_type:
        # parameter has distinct values
        param_val_expected_list_of_values = param_val_expected_type.split(',')[1].split('|')
        param_val_expected_type = param_val_expected_type.split(',')[0]
        print()


    if ('LIST[STR]' in param_val_expected_type.strip().upper()
            and 'LIST[STR]' in param_val_expected_type.strip()):
        # parameter value must be a list and exists and value can't be []
        print()

    elif ('LIST[str]' in param_val_expected_type.strip().upper()
            and 'LIST[str]' in param_val_expected_type.strip()):
        # parameter value must be a list and exists and can be []
        print()


    elif 'list[STR]' in param_val_expected_type.strip().upper():
        # parameter must be a list if exists and value can't be []
        print()

    elif 'list[str]' in param_val_expected_type.strip().upper():
        # parameter must be a list if exists and value can be []
        print()



    elif param_val_expected_type.replace(' ','').strip().upper() == 'ANY':
        # parameter value must exists
        print()

    elif param_val_expected_type.strip() == 'any':
        # parameter value may exists
        print()



    elif (param_val_expected_type.replace(' ', str()).strip().upper() == 'STR'
            and param_val_expected_type.strip() == 'STR'):
        p_logger.debug("Verify parameter ({param_key_name}) is a string and its value {p_param_value} exists")


    elif param_val_expected_type.strip().upper() == 'STR':
        # parameter value must be a string if it exists
        print()



    elif (param_val_expected_type.strip().upper() == 'INT'
            and param_val_expected_type.strip() == 'INT'):
        # parameter value must be a int and exists
        print()

    elif param_val_expected_type.strip().upper() == 'INT':
        # parameter value must be a int if it exists
        print()



    elif (param_val_expected_type.strip().upper() == 'FLOAT'
            and param_val_expected_type.strip() == 'FLOAT'):
        # parameter value must be a int and exists
        print()

    elif param_val_expected_type.strip().upper() == 'FLOAT':
        # parameter value must be a int if it exists
        print()






def VerifyDictKeys(p_dict_to_verify: dict,
                   p_dict_to_verify_against: []):

    logger = logging.getLogger(__file__)
    logging.basicConfig(level=logger.debug())



logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__file__)

logger.setLevel(logging.DEBUG)

verify(p_parameter_type=('table_name', 'INT'),
       p_param_value=18,
       p_logger=logger)
