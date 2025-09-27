from selenium import webdriver

from pages.crm_admin_login import AdminLoginPage


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

##---TEST DATA
base_url="http://49.249.28.218:8081/TestServer/Build/Small_CRM/admin/"

valid_username="admin"
valid_password="admin"

invalid_username="admin123"
invalid_password="admin123"

class TestAdminLogin:

    def test_successful_login(self):
        print("Testing successful login")

        ##---Initializing Login Page
        login_pg = AdminLoginPage(driver)

        print(f"Navigating to the base_url {base_url}")
        login_pg.navigate_to(base_url)
        assert login_pg.is_element_displayed(login_pg.ADMIN_LOGIN_PAGE_HEADER), "Login Page did not load properly"

        print(f"Logging in with Valid Credentials")
        login_pg.admin_login(valid_username, valid_password)
        assert login_pg.is_element_displayed(login_pg.DASHBOARD_PAGE_HEADER)

        print(f"Verifying successful login and Page Title")
        assert login_pg.is_login_successful(), "Login was not successful, dashboard page did not load"

        expected_title="CRM | Admin Dashboard"
        actual_title=login_pg.get_title()
        assert actual_title == expected_title, f"Actual title {actual_title} did not match expected title {expected_title}"


    def test_invalid_login(self):
        print("Testing invalid login")

        ##---Initializing Login Page
        login_pg = AdminLoginPage(driver)

        print(f"Navigating to the base_url {base_url}")
        login_pg.navigate_to(base_url)
        assert login_pg.is_element_displayed(login_pg.ADMIN_LOGIN_PAGE_HEADER), "Login Page did not load"

        print(f"Logging in with Invalid Credentials")
        login_pg.admin_login(invalid_username, invalid_password)

        print(f"Verifying invalid login and Page Title")
        expected_error_msg="*Invalid username or password"
        actual_error_msg=login_pg.get_error_msg()

        assert actual_error_msg == expected_error_msg, f"Actual error message {actual_error_msg} did not match expected error message"
        assert not login_pg.is_login_successful(), f"User should not be logged in with invalid credentials"
