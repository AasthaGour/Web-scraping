# import requests
# from bs4 import BeautifulSoup
# import random

# def scrapeWikiArticle(url):
# 	response = requests.get(
# 		url=url,
# 	)
	
# 	soup = BeautifulSoup(response.content, 'html.parser')

# 	title = soup.find(id="firstHeading")
# 	print(title.text)

# 	allLinks = soup.find(id="bodyContent").text
# 	print(allLinks)
 
# scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")

# import requests
# from bs4 import BeautifulSoup

# # Define the URL of the Wikipedia page
# url = "https://en.wikipedia.org/wiki/Web_scraping"

# # Send a GET request to the URL
# response = requests.get(url)

# # Create a BeautifulSoup object with the page content
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all the paragraphs on the page
# paragraphs = soup.find_all('p')

# # Loop through each paragraph and print the text
# for paragraph in paragraphs:
#     print(paragraph.get_text())


import requests
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object with the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the main content div
main_content = soup.find('div', id='mw-content-text')

# Find all the paragraphs, lists, and headers within the main content
content = main_content.find_all(['p', 'ul', 'ol', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Open a file in write mode
with open('scraped_text.txt', 'w', encoding='utf-8') as file:
    # Loop through each element and write the text to the file
    for element in content:
        # If the element is a header tag, write it in uppercase
        if element.name.startswith('h'):
            file.write(element.get_text().upper() + '\n')
        else:
            file.write(element.get_text() + '\n')
        file.write('\n')
