from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from etc import dir_func
from etc import time_func


def set_chrome_driver(headless_option, secret_mode):
    chrome_options = webdriver.ChromeOptions()

    if headless_option:
        chrome_options.add_argument('--headless')

    if secret_mode:
        chrome_options.add_argument('--incognito')  # 시크릿 모드

    driver = webdriver.Chrome(service=Service(ChromeDriverManager(log_level=40).install()), options=chrome_options)
    return driver


def make_screenshot_directory(directory, screenshot_directory_title):
    screenshot_directory = directory + screenshot_directory_title + '_스크린샷/'
    dir_func.mkdir_if_not_exist(directory=screenshot_directory)
    return screenshot_directory


def save_full_page_screenshot(driver, image_file_name, directory=''):
    width = driver.get_window_size()['width']
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(width=width, height=height)

    image_file = time_func.put_datetime_in_filename(file_type='png', file=directory + image_file_name, include_seconds=True)
    driver.find_element(By.TAG_NAME, 'body').screenshot(image_file)
    return image_file
