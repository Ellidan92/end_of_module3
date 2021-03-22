import time

def test_find_basket_buttton(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    basket_button = browser.find_element_by_css_selector('#add_to_basket_form button[type="submit"]' )
    assert basket_button, 'Not found this button on page'
    time.sleep(30)