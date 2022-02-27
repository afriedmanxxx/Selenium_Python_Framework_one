# import time
#
#
# def test_find_add_to_cart_button(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     browser.get(link)
#     # Если мы ищем elementS, то даже если элемент не найден, тест не упадет, вернется список с длиной 0,
#     # поэтому в данном случае NoSuchElementException не поможет, нужен Assert
#     buttons = browser.find_elements_by_class_name("btn-add-to-basket")
#     assert len(buttons) != 0, 'There is no "Add to cart" button'
#     time.sleep(5)

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()