import pytest
import random

@pytest.mark.ui
def test_login(index_page):
    index_page.input_username()
    index_page.input_password()
    index_page.press_login_btn()
    index_page.assertion_products()

'''random_numbers = [1,2,3]
@pytest.mark.smoke
def test_1():
    assert 1 == random.choice(random_numbers)'''


