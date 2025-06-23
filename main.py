import requests
import Playwright
import bs4

#Indeed 
#Make this into one list, and put sep file
known_job_boards = ["google.com", "linkedin.com", "indeed.com", "glassdoor.com", "monster.com"]
known_application_system = ["workday", "greenhouse", "lever"]

def parse_url():
    url = input("Enter the full URL of the job posting: ")

    # O (n) search
    for items in known_job_boards:
        if known_job_boards in url:
            print("Job board found")
            company_url = ask_company_url()
            verify_company_name(company_url)

        else:
            print("Assuming job is on company website")
            check_main_domain(url)

def check_main_domain(url):
    verify_company_name()

def verify_company_name(n):
    prompt = input(`Is your company name "${n}"? (y/n)`)

    if prompt == "y":
        print("Great!")
        #Send post req to snov.io
        find_company_contact_info()
    else:
        prompt = ask_company_url()
        verify_company_name(prompt)

def ask_company_url():
    company_url = input("Please enter the full URL of the MAIN company website (i.e google.com, statefarm.com)  you're applying for:")
    return company_url

def find_company_contact_info():
    # Send post request to snov.io
    pass

# SMTP check
def validate_email():
    pass

parse_url()
