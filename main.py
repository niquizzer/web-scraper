import requests
import bs4

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
            restult = print(soup.find('title'))
            if restult == None:
                print("No results found")


get_html()

