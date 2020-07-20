import logging
import logging.handlers
import time

def getLog(path="log\logtest\log.log"):
    log_file = path
    logger = logging.getLogger("m_id")
    logger.setLevel(level=logging.INFO)

    formatter = logging.Formatter('%(asctime)s/%(levelname)s/%(message)s')

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

def log_file(id):
    now = time.time()
    local_time = time.localtime(now)
    filename = time.strftime('%Y-%m-%d %H-%M-%S', local_time)
    date_format_localtime = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    print("log:"+id)
    with open('E:\\Desktop\\MovieRecommendationSystem\\log\\logfile\\' + filename + '.txt', mode='a', encoding='utf-8') as file:
        file.write(date_format_localtime+","+str(id))