from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def test_guest_can_add_item_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET)
        #self.is_element_present(*ProductPageLocators.BASKET), "Login form is not presented"
        login_link.click() 
        time.sleep(5)
    
    
 
        

