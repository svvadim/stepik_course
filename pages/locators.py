from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN = (By.ID, 'login_form')
    REGISTER = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, '')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success:first-child strong')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success:first-child')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
