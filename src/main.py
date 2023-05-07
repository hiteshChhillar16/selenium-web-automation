from arg_parser import parse_arguments
from web_app_automation import WebAppAutomation
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

try:
    # Parse arguments 
    args = parse_arguments()

    # Configure the Chrome web driver to ignore SSL errors and start maximized
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--start-maximized")


    # Create a WebAppAutomation instance with the modified Chrome options
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to a login page
    driver.get("https://devcorp.mdiachieve.com:12443/")

    # Create a WebAppAutomation instance
    automation = WebAppAutomation(driver, args)

    # Run the snf automation based upon passed arguements 
    automation.run()
except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)
    input("Presss Enter to close the browser...")

finally:
    input("Presss Enter to close the browser...")
    driver.quit()


