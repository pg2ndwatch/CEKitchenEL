from pathlib import Path
import sys
import json
import traceback

if Path(__file__).parent.parent not in sys.path:
    sys.path.append(Path(__file__).parent.parent)

if Path(__file__).parent not in sys.path:
    sys.path.append(Path(__file__).parent)

from CEKitchenEL import ElTableParamVerifier_lambda as lm





if __name__ == '__main__':
    context: str = ""
    event: dict = {"table_name": "tab_1",
                   "table_schema_name": "dbo",
                   "db_name": "database_name",
                   "db_port": "1433",
                   "db_instance": "hkkkkh",
                   "db_user": "pgadmin",
                   "db_password": "1#peanuts",
                   "db_max_retries": 2,
                   "row_count": 12000,
                   "column_list": ["col1","col2","col3","col4","col5"],
                   # "column_pk_list": ["col1"],
                   "data_type_list": ["int","varchar","varchar","varchar","varchar"],
                   "con_time_out_sec": 60,
                   "log_level": "debug"}


    lamda_return = lm.lambda_handler(event, context)


    print(f" Returned json {json.dumps(lamda_return)}")
