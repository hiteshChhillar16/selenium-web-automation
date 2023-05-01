from selenium_wrapper import SeleniumWrapper

class LoginPage:
    def __init__(self, driver, username, password):
        self.wrapper = SeleniumWrapper(driver)    
        self.username = username
        self.password = password
    
    def run(self):
        self.login()
    
    def login(self):
        # Locate the username and password input fields
        username_field = self.wrapper.find_element_by_id("username")
        password_field = self.wrapper.find_element_by_id("password")

        # Fill out the username and password fields
        self.wrapper.send_keys(username_field, self.username)
        self.wrapper.send_keys(password_field, self.password)

        # Locate the sign-in button
        signin_button = self.wrapper.find_element_by_id("loginbtn")

        # Click the sign-in button
        self.wrapper.click(signin_button)
