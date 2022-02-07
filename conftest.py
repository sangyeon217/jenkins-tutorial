import pytest
import logging
import logging_config


@pytest.fixture(scope="session")
def test_logger():
    logging_config.init()
    return logging.getLogger('test')
