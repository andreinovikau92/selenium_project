from .pages.product_page import ProductPage

def test_guest_can_add_item_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_item_to_basket()
    product_page = ProductPage(browser, browser.current_url)
    product_page.test_guest_can_add_item_to_basket()
    
