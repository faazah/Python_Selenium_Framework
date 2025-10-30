import logging
import allure

from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """
    Base class for all page objects. Contains common methods and properties that can be used
    across all pages object to maintain the DRY (Don't repeat yourself) principle
    """
    def __init__(self,driver):
        """
        Initialize BasePage with WebDriver instance and our central logger
        """
        self.driver=driver
        self.timeout=10
        self.wait=WebDriverWait(self.driver, self.timeout)
        self.logger=logging.getLogger(__name__)  #Get logger for this module

    @allure.step("Navigating to the base url: {base_url}")
    def navigate_to(self, base_url):
        try:
            self.driver.get(base_url)
            self.logger.info(f"Navigating to {base_url}")
        except:
            self.logger.error(f"Failed to navigate to {base_url}")
            raise

    @allure.step("Finding element by locator: {locator}")
    def find_element(self, locator):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            )
        except:
            self.logger.error(f"Failed to find element {locator} within {self.timeout} seconds")
            raise

    @allure.step("Clicking the element with locator: {locator}")
    def click(self, locator):
        element=self.find_element(locator)
        element.click()
        self.logger.info(f"Clicked the element {locator}")

    @allure.step("Entering the text: {text} with locator: {locator}")
    def enter_text(self, locator, text):
        element=self.find_element(locator)
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Entered text {text} on element {locator}")

    @allure.step("Getting the text from the element having locator: {locator}")
    def get_text(self, locator):
        element=self.find_element(locator)
        text = element.text
        self.logger.info(f"Retrieved text '{text}' from element: {locator}")
        return text

    @allure.step("Getting attribute value of attribute :{attr} with locator: {locator}")
    def get_attribute_value(self, locator, attr):
        element=self.find_element(locator)
        return element.get_attribute(attr)

    @allure.step("Checking whether the element is displayed or not with locator: {locator}")
    def is_element_displayed(self, locator):
        element=self.find_element(locator)
        return element.is_displayed()

    @allure.step("Getting the title of the page")
    def get_title(self):
        title=self.driver.title
        self.logger.info(f"Current title is {title}")
        return title

    @allure.step("Scrolling to an element with locator: {locator}")
    def scroll_to_element(self, locator):
        try:
            action_obj=ActionChains(self.driver)
            action_obj.scroll_to_element(locator).perform()
            self.logger.info(f"Scrolled to element {locator}")
        except:
            self.logger.error(f"Failed to scroll to element {locator}")
            raise

    @allure.step("Checking the visibility of the element having locator: {locator}")
    def is_visible(self, locator):
        try:
            self.wait.until(
                visibility_of_element_located(locator)
            )
            self.logger.info(f"Element is visible: {locator}")
            return True
        except:
            self.logger.error(f"Failed to find element {locator} within {self.timeout} seconds")
            return False