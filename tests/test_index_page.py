import pytest
import random
import allure


@allure.severity(allure.severity_level.BLOCKER)
@allure.description("testing successful log in ")
@allure.label("owner", "Oleg")
@pytest.mark.ui
def test_login(index_page):
    with allure.step("input valid username"):
        index_page.input_username()
    with allure.step("input valid pass"):
        index_page.input_password()
    with allure.step("press submit button"):
        index_page.press_login_btn()
    with allure.step("validate page title text"):
        index_page.assertion_products()



random_numbers = [1,2,3]
@pytest.mark.smoke
def test_1():
    assert 1 == random.choice(random_numbers)

@pytest.mark.sanity
def test_2():
    assert 2 == 3

'''name = "Oleg"
print(f"my name is {name}")

'''



