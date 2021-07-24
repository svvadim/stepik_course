from .locators import BaskedPageLocators
from .base_page import BasePage


class BaskedPage(BasePage):
    def should_be_text_empty_in_basked(self):
        assert 'empty' in self.browser.find_element(*BaskedPageLocators.BASKED_CONTENT).text, \
            'Basket not empty'

    def should_be_empty_basked(self):
        assert self.is_not_element_present(*BaskedPageLocators.BASKED_ITEM_FORM),\
            'Basket not empty'

    def should_not_be_text_empty_basked(self):
        assert self.is_not_element_present(*BaskedPageLocators.BASKED_CONTENT),\
            'Basket not empty'