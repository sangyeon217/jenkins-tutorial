import pytest
from etc import selenium_func
from etc import time_func
import logging
from file.log import logging_config
from FileDirectory import FileDirectory
import re


@pytest.fixture(scope="session")
def driver():
    driver = selenium_func.set_chrome_driver(headless_option=True, secret_mode=True)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def test_logger():
    logging_config.init()
    return logging.getLogger('test')


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if config.option.xmlpath:
        config.option.xmlpath = time_func.put_datetime_in_filename(file_type='xml', file=config.option.xmlpath, include_seconds=True)
    if config.option.htmlpath:
        config.option.htmlpath = time_func.put_datetime_in_filename(file_type='html', file=config.option.htmlpath, include_seconds=True)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    has_driver = 'driver' in item.fixturenames
    has_html_option = getattr(item.config, "_html", None)
    pytest_html = item.config.pluginmanager.getplugin("html")

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        fixture_extras = getattr(item.config, "extras", [])
        plugin_extras = getattr(report, "extra", [])

        if has_driver:
            driver = item.funcargs['driver']

        test_case_name = re.sub(pattern=r'::|\[', repl='_', string=re.sub(pattern=r'/', repl='__', string=re.sub(pattern=r'https?://|\]', repl='', string=report.nodeid)))
        xfail = hasattr(report, "wasxfail")
        if has_driver and has_html_option:
            if driver.current_url != 'data;,':  # URL 추가
                plugin_extras.append(pytest_html.extras.url(driver.current_url))

            if (report.skipped and xfail) or (report.failed and not xfail):
                parent_directory = FileDirectory(directory_type='report').directory
                screenshot_directory = selenium_func.make_screenshot_directory(directory=parent_directory, screenshot_directory_title='Failed')
                image_file = selenium_func.save_full_page_screenshot(driver=driver, image_file_name='Screenshot_'+test_case_name, directory=screenshot_directory)
                relative_path_image_file = image_file.lstrip(parent_directory)

                embedded_image = driver.get_screenshot_as_base64()
                plugin_extras.append(pytest_html.extras.image(embedded_image))
                plugin_extras.append(pytest_html.extras.url(relative_path_image_file, name='Screenshot'))
        elif has_driver:
            if (report.skipped and xfail) or (report.failed and not xfail):
                screenshot_directory = selenium_func.make_screenshot_directory(directory=FileDirectory(directory_type='screenshot').today_directory, screenshot_directory_title='Failed')
                selenium_func.save_full_page_screenshot(driver=driver, image_file_name=test_case_name, directory=screenshot_directory)

        report.extra = fixture_extras + plugin_extras
