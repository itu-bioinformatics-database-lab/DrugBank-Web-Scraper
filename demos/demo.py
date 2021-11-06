import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://go.drugbank.com/pharmaco/metabolomics")
soup = BeautifulSoup(page.content, 'html.parser')

print(page)

# with open("drug_demo.html", "w", encoding="utf-8") as file:
#     file.write(soup)
