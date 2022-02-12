import logging
import logging_config
import csv
logging_config.init()
logger = logging.getLogger()


def print_log():
    logger.error(msg='Jenkins Console Output 에 로그 스트림 출력이 남는지 확인')
    logger.debug(msg='DEBUG 로그 메세지')
    logger.info(msg='INFO 로그 메세지')
    logger.warning(msg='WARNING 로그 메세지')


def save_file(file_name):
    with open(file=file_name, mode='w', encoding='utf-8-sig', newline='') as f:
        fw = csv.writer(f)
        fw.writerow('TEST')


if __name__ == '__main__':
    print_log()
    save_file(file_name='test.txt')
