from selenium.webdriver.common.by import By

class BaseLocators:
    BUTTON_LOGIN_REGISTRATION = (By.XPATH, "//button[text()='Вход и регистрация']")
    BUTTON_NO_ACCOUNT = (By.XPATH, "//button[text()='Нет аккаунта']")
    BUTTON_ENTER_EMAIL = (By.NAME, "email")
    BUTTON_ENTER_PASSWORD = (By.NAME, "password")
    BUTTON_REPEAT_PASSWORD = (By.NAME, "submitPassword")
    BUTTON_CREATE_ACCONT = (By.XPATH, "//button[text()='Создать аккаунт']")
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выйти']")
    USER_PROFILE = (By.CSS_SELECTOR, "h3.profileText.name")
    AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    ERROR_MESSAGE =  (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")
    BUTTON_ADD_CARD = (By.XPATH, "//button[text()='Разместить объявление']")
    BUTTON_NEW_CARD = (By.XPATH, "//h1[text()='Новое объявление']")
