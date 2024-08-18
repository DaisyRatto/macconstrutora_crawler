import requests
from bs4 import BeautifulSoup
import pandas as pd
from a_selenium_get_source_from_all_frames import get_sourcecode_from_all_frames

url = 'https://mac.com.br/empreendimentos/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

page = requests.get(url, headers=headers, verify=False)

source = get_sourcecode_from_all_frames(page)

print(source)