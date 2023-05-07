from selenium_wrapper import SeleniumWrapper

class ElectronicFailedTransmissionsPage:
    def __init__(self, driver):
        self.driver = driver
        
    def run(self):
        self.driver.get("https://devcorp.mdiachieve.com:12443/module/orders/failed-transmissions?actionPageAlias=orders%2Ffailed-transmissions&zionpagealias=orders%2Ffailed-transmissions")