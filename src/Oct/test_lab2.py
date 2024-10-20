import pytest
import allure
@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

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