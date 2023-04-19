from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def test_guest_can_add_item_to_basket(self):
        #assert self.find_element(*ProductPageLocators.BASKET), "Basket is not presented"
        login_link = self.browser.find_element(*ProductPageLocators.BASKET)
        #self.is_element_present(*ProductPageLocators.BASKET), "Login form is not presented"
        login_link.click() 
    
    def test_book_name_marching(self):
        book_name = self.find_element()
            
        
    
    
 
        

