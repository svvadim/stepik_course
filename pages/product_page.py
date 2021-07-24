from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_add_to_basket()
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        link.click()
        self.should_be_message_to_adding()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), \
            "Button \"Add to cart\" is not presented"

    def should_be_message_to_adding(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_TO_ADDED_IN_BASKED) is not None, \
            "Message not view"

    def should_be_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME) is not None, "Product name is not present"

    def should_be_product_price(self):
        assert self.browser.find_element(ProductPageLocators.PRICE) is not None, "product price is not present"

    def should_be_basket_total_price(self):
        assert self.browser.find_element(ProductPageLocators.BASKET_MINI) is not None, "Price basket mini not present"

    #TODO add additional tests