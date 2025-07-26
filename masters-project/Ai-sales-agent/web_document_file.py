import requests
from bs4 import BeautifulSoup
import re

def GetData():
    urls =["https://www.strath.ac.uk/courses/postgraduatetaught/advancedcomputersciencewithdatasciencejanuary/"]
    text_data=""
    for url in urls:
        #response = requests.get(url)
        response = requests.get(url)
        
        soup =BeautifulSoup(response.text,'html.parser')
       # soup =BeautifulSoup(response.text, "html.parser")
        
        text =soup.get_text()
        text = re.sub(r"\[.*?\]", "", text)
        
        text=text.strip()
        text = re.sub(r"\[.*?\]", "", text)
        text_data +=  text +"\n\n"
        
         
        
    with open("data_strath.txt", "w", encoding="utf-8") as file:
        file.write(text_data)

    print("HTML data extracted and saved as webpages_strath.txt.")

    print(text_data)
    
GetData()