


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
         'column_pk_list': 'list[STR]',
         'data_type_list': 'list[STR],[float|int]',
         'con_time_out_sec': 'int',
         'log_level': 'str'}



def verify(p_val: tuple):
    key = p_val[0]
    val = p_val[1]
