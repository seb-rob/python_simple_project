import requests
from bs4 import BeautifulSoup
import time
import json
import re

# retry mechanism and data scraping function
def fetch_data_with_retries(url, retries=3, delay=2):
    """
        fetches data from url, if fails retries 3 times
        and finally returns
    """
    try:
        for attemp in range(retries):
            response = requests.get(url=url)
            response.raise_for_status()
            return response.text
    except requests.exceptions.RequestException as e:
        print(f"attempt {attemp + 1} failed {e}")
        if attemp < retries - 1:
            time.sleep(delay * (attemp + 1))        # exponential backoff
        else:
            raise

# function to extract data using BeautifulSoup and regual expression
def extract_data_from_html(html_content):
    """
        function extracts relevant data (link conntaining 'python' in it) from html content
    """
    if not html_content:
        raise ValueError("html content is invalid or empty!!")
    
    soup = BeautifulSoup(html_content, 'html.parser')
    titles = [];

    for link in soup.find_all('a', href=True):
        title = link.get_text()
        if re.match(r'.*python*.', title, re.IGNORECASE):       # looking for a link containing 'python'
            titles.append(title)

    return titles

# fuction to save data to a JSON file
def save_data_to_json(data, filename="scraped_data.json"):
    """
        function stores data(titles containing 'python') to jsonn file
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"data has been saved to {filename}")
    except Exception as e:
        print(f"Error saving data to file {e}")

# url
url = 'https://docs.python.org/3/'

# get html_content from url
data = fetch_data_with_retries(url=url)

# get all titles from given html cotennt
list_of_title = extract_data_from_html(data)

# save extracted data to json file
save_data_to_json(list_of_title);