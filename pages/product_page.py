from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    # Getters
    def _get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def _get_product_price_in_message(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text

    def _get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def _get_product_name_in_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text

    # Actions
    def click_to_button_add_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    # Expectations
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), \
            "Button \"Add to cart\" is not presented"

    def should_be_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text is not None, \
            "Product name is not present"

    def should_be_product_name_equal_product_name_in_message(self):
        assert self._get_product_name_in_message() == self._get_product_name(), \
            'Product name not equal product name in message'

    def should_be_product_price_equal_product_price_in_message(self):
        assert self._get_product_price_in_message() == self._get_product_price(), \
            'Product price not equal product price in message'

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE) is not None, \
            "Product price is not present"
