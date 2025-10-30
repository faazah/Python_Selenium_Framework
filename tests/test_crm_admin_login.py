import allure

from selenium import webdriver

from config.environment import Environment
from pages.crm_admin_login import AdminLoginPage


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

##---TEST DATA
invalid_username="admin123"
invalid_password="admin123"

@allure.feature("Authentication")
@allure.story("Admin Login")
class TestAdminLogin:
    """
    Test class for login functionality against Small CRM app.
    """
    @allure.title("Test Successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self):
        """
        Test Case: Verify successful login using valid Credentials from config.yaml file
        """
        ##---Initializing Login Page and variables
        login_pg = AdminLoginPage(driver)
        env = Environment('practice')
        base_url = env.get_base_url()
        username = env.get_username()
        password = env.get_password()

        # print(f"Navigating to the base_url {base_url}")
        with allure.step(f"Navigate to the Admin Login Page: {base_url}"):
            login_pg.navigate_to(base_url)
            assert login_pg.is_element_displayed(login_pg.ADMIN_LOGIN_PAGE_HEADER), "Login Page did not load properly"

        # print(f"Logging in with Valid Credentials")
        with allure.step(f"Perform login with valid Credentials"):
            login_pg.admin_login(username, password)
            assert login_pg.is_element_displayed(login_pg.DASHBOARD_PAGE_HEADER)

        # print(f"Verifying successful login and Page Title")
        with allure.step(f"Verify successful login and page title"):
            assert login_pg.is_login_successful(), "Login was not successful, dashboard page did not load"

            expected_title="CRM | Admin Dashboard"
            actual_title=login_pg.get_title()
            assert actual_title == expected_title, f"Actual title {actual_title} did not match expected title {expected_title}"

    @allure.title(f"Test Login failure with invalid credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_login(self):
        """
        Test Case: Verify invalid login using invalid Credentials.
        """

        ##---Initializing Login Page and Variables
        login_pg = AdminLoginPage(driver)
        env = Environment('practice')
        base_url = env.get_base_url()

        # print(f"Navigating to the base_url {base_url}")
        with allure.step(f"Navigating to the login page: {base_url}"):
            login_pg.navigate_to(base_url)
            assert login_pg.is_element_displayed(login_pg.ADMIN_LOGIN_PAGE_HEADER), "Login Page did not load"

        with allure.step(f"Perform login with invalid credentials"):
            # print(f"Logging in with Invalid Credentials")
            login_pg.admin_login(invalid_username, invalid_password)

        # print(f"Verifying invalid login and Page Title")
        with allure.step("Verifying invalid Login with error message"):
            expected_error_msg="*Invalid username or password"
            actual_error_msg=login_pg.get_error_msg()

            assert actual_error_msg == expected_error_msg, f"Actual error message {actual_error_msg} did not match expected error message"
            assert not login_pg.is_login_successful(), f"User should not be logged in with invalid credentials"
