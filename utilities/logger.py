import inspect
import logging as log


def log_method(logLevel=log.INFO):
    logger_name = inspect.stack()[1][3]

    logger = log.getLogger(logger_name)
    logger.setLevel(logLevel)

    fh = log.FileHandler('logfile.log')

    formatter = log.Formatter("******* %(message)s *********")

    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger

