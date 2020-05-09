import time
from selenium.webdriver.support.ui import WebDriverWait

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_add_to_basket_button(browser):
	browser.get(link)
	basket_button = len(browser.find_elements_by_class_name('btn-add-to-basket'))
	assert basket_button > 0, 'Basket not found'
