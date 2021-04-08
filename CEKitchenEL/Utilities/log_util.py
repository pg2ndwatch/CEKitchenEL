import logging



LOG_NAME_DICT = {'CRITICAL': 50,
                 'FATAL': 50,
                 'ERROR': 40,
                 'WARNING': 30,
                 'WARN': 30,
                 'INFO': 20,
                 'DEBUG': 10,
                 'NOTSET': 0}


LOG_LEVEL_OPTION_NAME_LIST:str = \
    'NOTSET|notset|DEBUG|debug|INFO|info|WARN|warn|WARNING|warning|' \
    'ERROR|error|CRITICAL|critical|FATAL|fatal'


def GetDebugLevelForName(p_log_level_name: str) -> int:

    assert p_log_level_name.strip().upper() in LOG_NAME_DICT.keys(), \
        f'Unknown debug level received ({p_log_level_name}. ' \
        f'Valid options are ({LOG_LEVEL_OPTION_NAME_LIST}))'

    return LOG_NAME_DICT[p_log_level_name.strip().upper()]



def GetDebugSession(p_session_name: str,
                    p_log_level_name: str) -> logging:

    log_level: int = GetDebugLevelForName(p_log_level_name)

    logging.basicConfig(level=p_log_level_name)

    logger = logging.getLogger(p_session_name)

    return logger



def ResetDebugLevel(p_logger: logging,
                    p_log_level_name: str) -> None:

    log_level: int = GetDebugLevelForName(p_log_level_name)
    p_logger.setLevel(log_level)










