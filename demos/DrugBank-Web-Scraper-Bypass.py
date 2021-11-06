import cloudscraper

# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session

url = "https://go.drugbank.com/pharmaco/metabolomics"

scraper = cloudscraper.create_scraper(browser='chrome', debug=True)

print(scraper.get(url).text)