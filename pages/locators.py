from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REG_EMAIL = (By.NAME, 'registration-email')
    REG_PASS1 = (By.NAME, 'registration-password1')
    REG_PASS2 = (By.NAME, 'registration-password2')
    REG_BUTTON = (By.NAME, 'registration_submit')
    LOGIN = (By.NAME, 'login-username')
    PASS = (By.NAME, 'login-password')
    LOGIN_BUTTON = (By.NAME, 'login_submit')


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
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group .btn-default:first-child')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BaskedPageLocators:
    BASKED_CONTENT = (By.CSS_SELECTOR, '#content_inner p')
    BASKED_ITEM_FORM = (By.CSS_SELECTOR, '#basket_formset')
