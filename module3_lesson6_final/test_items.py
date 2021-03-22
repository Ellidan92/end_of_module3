def test_language(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    basket = browser.find_element_by_css_selector('#add_to_basket_form button[type="submit"]' )
    assert basket, f'element {basket} not found on this page'