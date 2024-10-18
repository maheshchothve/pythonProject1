import pytest


@pytest.mark.skip
def test_method():
    print("hello")
    assert 2+2==4

@pytest.mark.smoke
def test_tc2():
    print("test case no 2")
    assert 3-0==3
    assert 2+2==4

@pytest.mark.reg
def test_tc3():
    print("test case no 3py")