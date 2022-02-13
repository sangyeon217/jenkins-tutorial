def test_sample1():
    assert True


def test_sample2(test_logger):
    test_logger.error(msg='Test Failed')
    assert False


def test_sample3(driver):
    url = "https://github.com/sangyeon217/jenkins-tutorial"
    driver.get(url)
    assert False
