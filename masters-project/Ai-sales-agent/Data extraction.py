import requests
from bs4 import BeautifulSoup
import re

# List of URLs of the webpages you want to extract HTML data from
#urls = ["https://www.fctraining.org/fc-data-science-machine-learning-ai-course.php"]
urls=["https://www.strath.ac.uk/courses/postgraduatetaught/advancedcomputersciencewithdatasciencejanuary/"]
# Create an empty string to store the extracted text
text_data = ""

# Iterate over each URL
for url in urls:
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Remove HTML tags and schema tags
    text = soup.get_text()
    text = re.sub(r"\[.*?\]", "", text)  # Remove schema tags
    
    # Remove leading and trailing whitespaces
    #text = text.strip()
    text = text.strip()
    
    # Append the extracted text to the main text_data string
    text_data += text + "\n\n"

# Save the cleaned text data as a .txt file
with open("webpages_strath.txt", "w", encoding="utf-8") as file:
    file.write(text_data)

print("HTML data extracted and saved as webpages_strath.txt.")

print(text_data)

