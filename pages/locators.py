from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN = (By.ID, 'login_form')
    REGISTER = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.price_color')
    BASKET_MINI = (By.CSS_SELECTOR, '.basket-mini')
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    MESSAGE_TO_ADDED_IN_BASKED = (By.CSS_SELECTOR, '.alertinner')
