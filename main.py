import requests
import bs4
# from validate_email import validate_email

# The problem is we want to build a repeatable scraper
# that can find a recruiters email address based on the job title
# and company name.  
#
# The inputs is the job title, company name, job location
# job posting url, and the date of when the job was posted
#
# The output is the name, email address, and phone number of the recruiter
#
#

#Edge cases
test = {
    'input': {
        'job title': 'Software Engineer',
        'company name': 'Google',
        'job location': 'San Francisco, CA',
        'job posting url': 'https://careers.google.com/jobs/results/10001270/',
        'date of posting': '2021-01-01',
        'application platform': 'indeed',
        'keywords': ['software engineer', 'google', 'san francisco', 'ca'],
    },
    'output': {
        'name': 'John Doe',
        'email': 'johndoe@gmail.com',
        'phone': '555-555-5555',
        'linkedin': 'linkedin.com/in/johndoe',
    }
}
#Can't find application platform 
test.update({
    'input': {
        'job title': 'Software Engineer',
        'company name': 'Google',
        'job location': 'San Francisco, CA',
        'job posting url': 'https://careers.google.com/jobs/results/10001270/',
        'date of posting': '2021-01-01',
        'application platform': 'indeed',
        'keywords': ['software engineer', 'google', 'san francisco', 'ca'],
    },
    'output': {
        'name': 'John Doe',
        'email': 'johndoe@gmail.com',
        'phone': '555-555-5555',
        'linkedin': 'linkedin.com/in/johndoe',
    }
})
#Missing some inputs
test.update({
    'input': {
        'job title': 'Software Engineer',
        'company name': '',
        'job location': 'San Francisco, CA',
        'job posting url': 'https://careers.google.com/jobs/results/10001270/',
        'date of posting': '',
        'application platform': '',
        'keywords': ['software engineer', 'google', 'san francisco', 'ca'],
    },
    'output': {
        # Maybe find some inputs but not all
        'name': 'John Doe',
        'email': 'johndoe@gmail.com',
        'phone': '',
        'linkedin': 'linkedin.com/in/johndoe',
    }
})
# No viable inputs
test.update({
    'input': {
        'job title': '',
        'company name': '',
        'job location': '',
        'job posting url': '',
        'date of posting': '',
        'application platform': '',
        'keywords': [''],
    },
    'output': 'Information not found'
})
# Company name recruiter name found, but no contact info
test.update({
    'input': {
        'job title': '',
        'company name': 'vanguard',
        'recruiter name': 'John Doe',
        'job location': '',
        'job posting url': '',
        'date of posting': '',
        'application platform': '',
        'keywords': [''],
    },
    'output': {
        #Guessing email based on common formats
        'Name': 'John Doe',
        'email': 'johndoe@gmail.com',
    }
})

# 1. Get request to website job posting site, parse html for relevant information (company name,
# job title, location, company url), if we can find the information we need,
# return the information, otherwise go to the next step
# 2. Based on inputs, send get requests to other site w/ headless br w/ custom queries
# using input data. 
# ---------Some example places: LinkedIn, Google, Indeed, Company website, Facebook
# 3. Parse the information from the other databases. See if we can find at least name and 
# contact info.
# 4. Return the information if found, otherwise skip values not found
# ---------If we can find the name and company but not the email, we can guess the email
# by using common formats, then validate that email w/ SMTP check. 
# 5. Export data to csv

#Inputs for the scraper
inputs = ['h1', 'p']

alt_sites_search = ['https://google.com', 'https://linkedin.com', 'https://facebook.com']

recruitment_sources = {
    "linkedin": "linkedin.com/in/",
    "google": "google.com/search?q=",
    "indeed": "indeed.com/jobs?q=",
    "facebook": "facebook.com/search/top/?q=",
    "twitter": "twitter.com/search?q=",
    "instagram": "instagram.com/explore/tags/",
    "youtube": "youtube.com/results?search_query=",
    'email_finder_tools': [
        'https://hunter.io/search?query=',
        'https://www.emailfinder.io/search?q=',
        'https://www.findemail.info/search?q=',
        'https://www.email-checker.net/search?q=',
        'https://www.email-checker.net/search?q=',
        'https://clearout.io'
    ]
}

def get_html():
    url = input("Enter a URL: ")
    value = False

    if url == "":
        value = False
        print("Please enter a valid URL")
        return
    else:
        r = requests.get(url);
        parse_html(r)

def parse_html(r):
    html = r.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    #find specific values
    result = soup.find_all('jobsearch')

    for i in result:
        print(i.get_text())

    if result == None:
        print("No results found")

def no_url_found():

    pass

def search_alt_sites():
    pass

def validate_email():
    #SMTP check
    pass

get_html()
