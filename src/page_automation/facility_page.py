from selenium.common.exceptions import NoSuchElementException

from selenium_wrapper import SeleniumWrapper

class FacilityPage:
    def __init__(self, driver, facility_name):
        self.wrapper = SeleniumWrapper(driver)
        self.facility_name = facility_name
    
    def run(self):
        self.select_facility()
        
    def select_facility(self):
        
        # Check if the desired facility is found
        facility_link = self.find_facility_link()
        if facility_link is None:

            # Go to Facility Search page
            self.wrapper.go_to_search_facility_page()

            # Select the desired facility
            facility_name_field = self.wrapper.find_element_by_name("facility_name")
            self.wrapper.send_keys(facility_name_field,self.facility_name)
            searchButton = self.wrapper.find_element_by_name("search")
            self.wrapper.click(searchButton)
            
            # Locate the table with the id "facilitySearchList"
            table_xpath = '//*[@id="facilitySearchList"]'
            
            # Create an XPath expression to find all clickable links in the first column of the table
            links_xpath = f'{table_xpath}//tr/td[1]/a'
            
            # Locate all the clickable links in the first column using the XPath expression
            facility_links = self.wrapper.find_elements_by_xpath(links_xpath)
            
            # If there's at least one facility link, click on the first one
            if facility_links:
                facility_links[0].click()
            else:
                print("No facility links found.")                                    
    
    def find_facility_link(self):
        try:
            # Create an XPath expression that finds the link element containing the facility name
            xpath_expression = f'//span[contains(., "Facility:")]/a[contains(., "{self.facility_name}")]'

            # Locate the link element using the XPath expression
            facility_link = self.wrapper.find_element_by_xpath(xpath_expression)
            return facility_link
        except NoSuchElementException:
                return None
        