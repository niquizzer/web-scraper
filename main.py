import requests
import bs4

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
    }
    'output': {
        'name': 'John Doe',
        'email': 'johndoe@gmail.com',
        'phone': '555-555-5555',
        'linkedin': 'linkedin.com/in/johndoe',
    }
}
#Can't find application platform 
test.append({
    'input': {
        'job title': 'Software Engineer',
        'company name': 'Google',
        'job location': 'San Francisco, CA',
        'job posting url': 'https://careers.google.com/jobs/results/10001270/',
        'date of posting': '2021-01-01',
        'application platform': 'indeed',
        'keywords': ['software engineer', 'google', 'san francisco', 'ca'],
    }
    'output': {
        'name': 'John Doe',
        'email': 'johndoe@gmail.com',
        'phone': '555-555-5555',
        'linkedin': 'linkedin.com/in/johndoe',
    }
})
#Missing some inputs
test.append({
    'input': {
        'job title': 'Software Engineer',
        'company name': '',
        'job location': 'San Francisco, CA',
        'job posting url': 'https://careers.google.com/jobs/results/10001270/',
        'date of posting': '',
        'application platform': '',
        'keywords': ['software engineer', 'google', 'san francisco', 'ca'],
    }
    'output': {
        # Maybe find some inputs but not all
        'name': 'John Doe',
        'email': 'johndoe@gmail.com',
        'phone': '',
        'linkedin': 'linkedin.com/in/johndoe',
    }
})
# No viable inputs
test.append({
    'input': {
        'job title': '',
        'company name': '',
        'job location': '',
        'job posting url': '',
        'date of posting': '',
        'application platform': '',
        'keywords': [''],
    }
    'output': 'Information not found'
})
# Company name recruiter name found, but no contact info
test.append({
    'input': {
        'job title': '',
        'company name': 'vanguard',
        'recruiter name': 'John Doe',
        'job location': '',
        'job posting url': '',
        'date of posting': '',
        'application platform': '',
        'keywords': [''],
    }
    'output': {
        #Guessing email based on common formats
        'Name': 'John Doe',
        'email': 'johndoe@gmail.com',
    }
})

# 1. Get request to website, parse html for relevant information
# 2. Based on inputs, send get requests to other major info dabaseses w/ custom queries
# using input data or headless browsers. We can start with the job listing page itself
# to see if we can find the information we need.
# ---------Some example places: LinkedIn, Google, Indeed, Company website, Facebook
# 3. Parse the information from the other databases
# 4. Return the information if found, otherwise skip values not found
# ---------If we can find the name and company but not the email, we can guess the email
# by using common formats, then validate that email w/ SMTP check. 
# 5. Stonks

def get_html():
    url = input("Enter a URL: ")
    value = False

    if url == "":
        value = False
        print("Please enter a valid URL")
        return
    else:
        r = requests.get(url);
        value = True
        
        if value == True:
            html_doc = r.text
            soup = bs4.BeautifulSoup(html_doc, 'html.parser')
            result = print(soup.find('p'))
            if result == None:
                print("No results found")


get_html()
