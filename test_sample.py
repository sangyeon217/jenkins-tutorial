def test_sample1():
    assert True


def test_sample2(test_logger):
    test_logger.error(msg='Test Failed')
    assert False
