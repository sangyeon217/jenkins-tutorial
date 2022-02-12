import logging
import logging_config
import file_func
import html_func
import time_func
import csv
logging_config.init()
logger = logging.getLogger()


def print_log():
    logger.error(msg='Jenkins Console Output 에 로그 스트림 출력이 남는지 확인')
    logger.debug(msg='DEBUG 로그 메세지')
    logger.info(msg='INFO 로그 메세지')
    logger.warning(msg='WARNING 로그 메세지')


def save_file(file):
    with open(file=file, mode='w', encoding='utf-8-sig', newline='') as f:
        fw = csv.writer(f)
        fw.writerow('TEST'.split(','))


def save_html_file(file, html_title):
    html_func.create(html_file=file, html_title=html_title)


if __name__ == '__main__':
    print_log()
    text_file = 'test.txt'
    save_file(file=text_file)
    html_file = 'file/html/example.html'
    save_html_file(file=time_func.put_datetime_in_filename(file_type='html', file=html_file, include_seconds=True), html_title=file_func.convert_file_to_text(file=text_file))
