from page_automation.login_page import LoginPage
from page_automation.facility_page import FacilityPage
from page_automation.resident_page import ResidentPage
from page_automation.electronic_failed_transmissions_page import ElectronicFailedTransmissionsPage

class WebAppAutomation:
    def __init__(self, driver, args):
        self.driver = driver
        self.args = args
        self.pages = {
            "facilitysearch": FacilityPage,
            "residentpage": ResidentPage,
            "failedtransmissions": ElectronicFailedTransmissionsPage
            # Add more pages here
        }

    def run(self):
        # Call the login method from LoginPage
        login_page = LoginPage(self.driver, self.args.username, self.args.password)
        login_page.login()

        # Perform the action based on the provided page_name
        if self.args.page == "facilitysearch":
            facility_page = self.pages["facilitysearch"](self.driver, self.args.facility_name)
            facility_page.run()

        elif self.args.page == "residentpage":
            # Ensure FacilityPage is executed before ResidentPage
            facility_page = self.pages["facilitysearch"](self.driver, self.args)
            facility_page.run()

            resident_page = self.pages["residentpage"](self.driver, self.args)
            resident_page.run()
            
        elif self.args.page == "failedtransmissions":
            # Ensure FacilityPage is executed before ResidentPage
            facility_page = self.pages["facilitysearch"](self.driver, self.args.facility_name)
            facility_page.run()

            failed_transmissions_page = self.pages["failedtransmissions"](self.driver)
            failed_transmissions_page.run()            

        else:
            print(f"Unknown page name: {self.args.page}")

