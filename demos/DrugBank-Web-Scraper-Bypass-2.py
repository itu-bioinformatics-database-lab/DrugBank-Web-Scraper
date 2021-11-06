import cfscrape

url = "https://go.drugbank.com/pharmaco/metabolomics"
scraper = cfscrape.create_scraper(delay=15)  # returns a CloudflareScraper instance

# Or: scraper = cfscrape.CloudflareScraper()  # CloudflareScraper inherits from requests.Session
print(scraper.get(url).content)  # => "<!DOCTYPE html><html><head>..."