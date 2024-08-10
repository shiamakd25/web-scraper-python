import requests
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """Scrape the page source from the url"""
    response = requests.get(url)
    source = response.text
    return source

