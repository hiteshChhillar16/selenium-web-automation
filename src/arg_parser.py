import argparse

def parse_arguments():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Automate your company's web application")

    # Add arguments
    parser.add_argument("-p", "--page", type=str, choices=["facilitysearch", "residentpage", "failedtransmissions"], help="Page name")
    parser.add_argument("-f", "--first", type=str, help="Resident's first name")
    parser.add_argument("-l", "--last", type=str, help="Resident's last name")
    parser.add_argument("-c", "--facility_name", type=str, help="Facility name")
    parser.add_argument("-u", "--username", type=str, help="Username for authentication")
    parser.add_argument("-P", "--password", type=str, help="Password for authentication")

    # Parse arguments
    return parser.parse_args()
