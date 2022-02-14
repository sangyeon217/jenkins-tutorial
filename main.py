import logging
from file.log import logging_config
from etc import selenium_func
from etc import file_func
from etc import html_func
from etc import time_func
from FileDirectory import FileDirectory
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


def save_screenshot():
    driver = selenium_func.set_chrome_driver(headless_option=True, secret_mode=True)
    url = "https://github.com/sangyeon217/jenkins-tutorial"
    try:
        driver.get(url)
        selenium_func.save_full_page_screenshot(driver=driver, image_file_name='Screenshot.png', directory=FileDirectory(directory_type='screenshot').today_directory)
    finally:
        driver.quit()


def print_user_agent():
    driver = selenium_func.set_chrome_driver(headless_option=True, secret_mode=True)
    url = "https://github.com/sangyeon217/jenkins-tutorial"
    try:
        driver.get(url)
        user_agent = driver.execute_script("return navigator.userAgent;")
        print(user_agent)
    finally:
        driver.quit()


if __name__ == '__main__':
    print_log()
    text_file = 'test.txt'
    save_file(file=text_file)
    save_html_file(file=time_func.put_datetime_in_filename(file_type='html', file=FileDirectory(directory_type='html').directory + 'example.html', include_seconds=True), html_title=file_func.convert_file_to_text(file=text_file))
    save_screenshot()
    print_user_agent()
