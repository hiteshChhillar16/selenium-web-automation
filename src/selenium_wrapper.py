from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, value):
        return self.driver.find_element(By.ID, value)
    
    def find_element_by_name(self, value):
        return self.driver.find_element(By.NAME, value)
    
    def find_element_by_xpath(self, value):
        return self.driver.find_element(By.XPATH, value)         

    def send_keys(self, element, keys):
        element.send_keys(keys)

    def click(self, element):
        element.click()

    def wait_for_element(self, by, value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, value)))
    
    def find_facility_link(self, facility_name):
        # Create an XPath expression that finds the link element containing the facility name
        xpath_expression = f'//span[contains(., "Facility:")]/a[contains(., "{facility_name}")]'

        # Locate the link element using the XPath expression
        facility_link = self.find_element(self, By.XPATH, xpath_expression)
        return facility_link
    
    def go_to_search_facility_page(self):
        self.driver.get("https://devcorp.mdiachieve.com:12443/Zion?zionpagealias=FACILITYSEARCH")

