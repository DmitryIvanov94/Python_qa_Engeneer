import pytest


@pytest.fixture(scope="function")
def set_correct():
    return {'Hellow', 'Vasia', 'Hellow', 'hi'}


@pytest.fixture(scope="function")
def list_correct():
    return ['Hellow', 'Vasia', 'Hellow', 'hi', '111']


@pytest.fixture(scope="function")
def dict_correct():
    return {'Hellow': 'Vasia', 'hi': '111'}
