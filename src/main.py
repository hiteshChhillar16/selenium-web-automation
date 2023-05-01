from arg_parser import parse_arguments
from web_app_automation import WebAppAutomation
from selenium import webdriver


# Parse arguments 
args = parse_arguments.arguments()

# Configure the Chrome web driver
driver = webdriver.Chrome()

# Navigate to a login page
driver.get("https://devcorp.mdiachieve.com:12443/")

# Create a WebAppAutomation instance
automation = WebAppAutomation(driver, args)

# Run the snf automation based upon passed arguements 
automation.run()


