from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.timeout=10

    def navigate_to(self, base_url):
        try:
            self.driver.get(base_url)
            print(f"Navigating to {base_url}")
        except:
            print(f"Failed to navigate to {base_url}")
            raise

    def find_element(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except:
            print(f"Failed to find element {locator} within {self.timeout} seconds")
            raise

    def click(self, locator):
        element=self.find_element(locator)
        element.click()
        print(f"Clicked the element {locator}")

    def enter_text(self, locator, text):
        element=self.find_element(locator)
        element.clear()
        element.send_keys(text)
        print(f"Entered text {text} on element {locator}")

    def get_text(self, locator):
        element=self.find_element(locator)
        return element.text

    def get_attribute_value(self, locator, attr):
        element=self.find_element(locator)
        return element.get_attribute(attr)

    def is_element_displayed(self, locator):
        element=self.find_element(locator)
        return element.is_displayed()

    def get_title(self):
        title=self.driver.title
        print(f"Current title is {title}")
        return title

    def scroll_to_element(self, locator):
        try:
            action_obj=ActionChains(self.driver)
            action_obj.scroll_to_element(locator).perform()
            print(f"Scrolled to element {locator}")
        except:
            print(f"Failed to scroll to element {locator}")
            raise

    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                visibility_of_element_located(locator)
            )
            print(f"Element is visible: {locator}")
            return True
        except:
            print(f"Failed to find element {locator} within {self.timeout} seconds")
            return False