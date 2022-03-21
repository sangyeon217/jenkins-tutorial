import main
main.print_log()


def test_sample1(test_logger):
    test_logger.debug(msg='Passed Test: DEBUG LOG MESSAGE')
    test_logger.info(msg='Passed Test: INFO LOG MESSAGE')
    test_logger.warning(msg='Passed Test: WARNING LOG MESSAGE')
    test_logger.error(msg='Passed Test: ERROR LOG MESSAGE')
    assert True


def test_sample2(test_logger):
    test_logger.error(msg='Test Failed')
    assert False


def test_sample3(driver):
    url = "https://github.com/sangyeon217/jenkins-tutorial"
    driver.get(url)
    assert False
