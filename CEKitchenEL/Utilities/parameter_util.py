from typing import NamedTuple, Any
from pathlib import Path
import sys
import json


if Path(__file__).parent.parent not in sys.path:
    sys.path.append(Path(__file__).parent.parent)

if Path(__file__).parent not in sys.path:
    sys.path.append(Path(__file__).parent)

from . import log_util as lu


class VerifiedParamReturnNT(NamedTuple):
    """
    : parameter_found: The event dictionary of parameters sent to lambda!
    :return: tuple: parameter_name - The name of the parameter
                    parameter_found - True if the parameter was found
                    parameter_value_valid - True if the parameter value is valid
                    parameter_value - if parameter_found should be set to default value if exist
    """
    param_name: str = ''
    param_found: bool = False
    param_value_valid: bool = False
    param_value: Any = str()




def VerifyParameter(p_param_name: str,
                    p_params_dict: dict,
                    p_default_value: any,
                    p_valid_value_list: [Any] = None) -> VerifiedParamReturnNT:
    """
    :param p_valid_value_list: a list of valid values
    :param p_param_name: The name of the parameter
    :param p_params_dict: The event dictionary of parameters sent to lambda!
    ;param p_default_value: Default value to use if not found
    :return: named tuple ParameterReturnNT:
    """



    param_value: any = ''
    param_found: bool = False
    param_value_valid: bool = False
    valid_value_list: [any]

    if p_valid_value_list is None:
        valid_value_list = []
    else:
        valid_value_list = p_valid_value_list
        assert p_default_value in lu.LOG_LEVEL_OPTION_NAME_LIST, \
            f'Unknown debug level received for default value ({p_default_value})'

    return_value: VerifiedParamReturnNT

    if p_param_name.lower() in p_params_dict.keys():
        param_value = p_params_dict[p_param_name.lower()]
        param_found = True
        param_value_valid = (valid_value_list == [] or param_value in valid_value_list)

    elif p_param_name.upper() in p_params_dict.keys():
        param_value = p_params_dict[p_param_name.upper()]
        param_found = True
        param_value_valid = (valid_value_list == [] or param_value in valid_value_list)

    else:
        param_found = False
        param_value = p_default_value
        param_value_valid = True


    return_var = VerifiedParamReturnNT(param_name=p_param_name,
                                       param_found=param_found,
                                       param_value_valid=param_value_valid,
                                       param_value=param_value)

    return return_var
