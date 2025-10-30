from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdminLoginPage(BasePage): #Make AdminLoginPage inherit from BasePage
    """
    Page Object for the Admin Login page (Small CRM)
    """
    ##---Locators
    ADMIN_LOGIN_PAGE_HEADER=(By.XPATH, '//h2[text()="Sign in to CRM Admin"]')
    USERNAME_FIELD= (By.XPATH, '//input[@id="txtusername"]')
    PASSWORD_FIELD=(By.XPATH, '//input[@id="txtpassword"]')
    LOGIN_BTN=(By.XPATH, '//button[@name="login"]')
    ERROR_MSG=(By.XPATH, '//p[text()="*Invalid username or password"]')
    DASHBOARD_PAGE_HEADER=(By.XPATH, '//a[contains(text(), "Admin")]')

    def __init__(self, driver):
        super().__init__(driver)

    def admin_login(self, username, password):
        """
        Performs a full login action using methods inherited from BasePage
        """
        self.logger.info(f"Attempting to Login to CRM Admin with username: {username}")
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)
        # Note: We don't need to return True/False. If any step fails, an exception will be raised.

    def is_login_successful(self):
        """
        Checks if login was successful by looking for an element on the Dashboard page.
        Uses the is_visible method inherited from BasePage
        """
        # return self.is_element_displayed(self.DASHBOARD_PAGE_HEADER)
        return self.is_visible(self.DASHBOARD_PAGE_HEADER)


    def get_error_msg(self):
        """
        Gets the text of the login error message
        """
        if self.is_element_displayed(self.ERROR_MSG):
            return self.get_text(self.ERROR_MSG)
        return "No error message found"