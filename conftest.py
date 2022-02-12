import pytest
import time_func
import logging
import logging_config


@pytest.fixture(scope="session")
def test_logger():
    logging_config.init()
    return logging.getLogger('test')


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if config.option.htmlpath:
        config.option.htmlpath = time_func.put_datetime_in_filename(file_type='html', file=config.option.htmlpath, include_seconds=True)
