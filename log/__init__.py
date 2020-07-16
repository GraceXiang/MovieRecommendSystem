import logging
import logging.handlers


def getLog(path="log\logfile\log.log"):
    log_file = path
    logger = logging.getLogger("m_id")
    logger.setLevel(level=logging.INFO)

    formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    file_handler = logging.handlers.TimedRotatingFileHandler(filename=log_file,
                                                    when="S",
                                                    interval=1,
                                                    backupCount=0,
                                                    encoding='utf-8')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

# global logger
logger=getLog()