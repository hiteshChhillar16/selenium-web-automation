from selenium_wrapper import SeleniumWrapper

class ResidentPage:
    def __init__(self, driver, args):
        self.wrapper = SeleniumWrapper(driver)