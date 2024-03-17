from test_runner import test_runner

def test_hello():
    test_runner.hello('abc')
    assert True