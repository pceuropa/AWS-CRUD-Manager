import logging
from telemetry.config.config_parser import settings

'''
10 DEBUG 	Detailed information, typically of interest only when diagnosing problems.
20 INFO 	Confirmation that things are working as expected.
30 WARNING	An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
40 ERROR 	Due to a more serious problem, the software has not been able to perform some function.
50 CRITICAL     Serious error, indicating that the program itself may be unable to continue running

%(pathname)s Full pathname of the source file where the logging call was issued(if available).
%(filename)s Filename portion of pathname.
%(module)s Module (name portion of filename).
%(funcName)s Name of function containing the logging call.
%(lineno)d Source line number where the logging call was issued (if available).

'''


def simple_logger(config):
    """This logger work as one in all files. Than better use setup_logger
    :config: dict
    :returns: logging.logger
    """
    logging.basicConfig(**config)
    return logging.getLogger(__name__)


def setup_logger(config):
    """Function setup as many loggers as you want
    :config: dict
    :returns: logging.logger
    """
    name = config['filename'].split('.')[0]
    config['filename'] = f"{settings['folder_log']}/{config['filename']}"

    formatter = logging.Formatter(config['format'])
    handler = logging.FileHandler(config['filename'])
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(config['level'])
    logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    pass
