from alexpackagetest import __version__
from .alexpackagetest import alexpackagetestmodule


def test_version():
    assert __version__ == '0.1.0'


def test_concatenator():
    actual = concatenator('test', 'ing')
    expected = 'testing'
    assert actual == expected
