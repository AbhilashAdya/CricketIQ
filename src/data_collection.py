import requests
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
import os

url_new =["https://www.iplt20.com/teams"]

def access(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    

    try:
        print(f"🔍 Accessing: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            print(f"✅ Success! Page title: {soup.title.text if soup.title else 'No title'}")
            return soup
            
        elif response.status_code == 403:
            print(f"❌ 403 Forbidden - Access denied for {url}")
            return None
        elif response.status_code == 404:
            print(f"❌ 404 Not Found - {url}")
            return None
        else:
            print(f"❌ Status {response.status_code} for {url}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error accessing {url}: {e}")
        return None


url_content = [access(url) for url in url_new]

if url_content[0] is not None:
    
    path = os.path.join(os.getcwd(), "data","raw", "ipl_match_page.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(str(url_content[0]))
        print("Successfully written html content!!!")
        