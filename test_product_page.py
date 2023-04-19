from .pages.product_page import ProductPage
from .pages.base_page import BasePage

def test_guest_can_add_item_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)
    alert = BasePage (browser, link)
    page.open()
    page.test_guest_can_add_item_to_basket() 
    alert.solve_quiz_and_get_code()
    #product_page = ProductPage(browser, browser.current_url)
    #product_page.test_guest_can_add_item_to_basket()
    
    #alert.switch_to.alert
    #alert_product.solve_quiz_and_get_code()


        