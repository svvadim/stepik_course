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
            f'Button \'Add to cart\' is not presented [URL:{self.current_url}]'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def should_be_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text is not None, \
            f'Product name is not present [URL:{self.current_url}]'

    def should_be_product_name_in_message(self):
        assert self._get_product_name_in_message() == self._get_product_name(), \
            f'Product name not equal product name in message [URL:{self.current_url}]'

    def should_be_product_price_in_message(self):
        assert self._get_product_price_in_message() == self._get_product_price(), \
            f'Product price not equal product price in message [URL:{self.current_url}]'

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE) is not None, \
            f'Product price is not present [URL:{self.current_url}]'
