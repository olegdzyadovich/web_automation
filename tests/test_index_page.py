
def test_login(index_page):
    index_page.input_username()
    index_page.input_password()
    index_page.press_login_btn()
    index_page.assertion_products()

