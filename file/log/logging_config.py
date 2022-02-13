import logging
import logging.config

log_level_dict = {
    'NOTSET': 0,
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'SEVERE': 40,
    'ERROR': 40,
    'CRITICAL': 50
}

logging.basicConfig(
    filename='file/log/app.log',
    filemode='a',
    format='%(levelname)-8s %(asctime)s %(name)s:: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)


def init():
    logging.config.fileConfig(fname='file/log/logging.ini')


def rtn_log_level(log_level):
    return log_level_dict.get(log_level)


def save_browser_logs(logger, driver, msg):
    browser_logs = driver.get_log('browser')
    for browser_log in browser_logs:
        rec = logger.makeRecord(
            name="%s.%s" % (logger.name, browser_log['source']),
            level=rtn_log_level(browser_log['level']),
            fn='.',
            lno=0,
            msg="%s : %s" % (msg, browser_log['message']),
            args=None,
            exc_info=None
        )
        rec.created = browser_log['timestamp'] / 1000
        logger.handle(rec)
