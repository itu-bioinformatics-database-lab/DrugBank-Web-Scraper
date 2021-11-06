import undetected_chromedriver as uc

driver = uc.Chrome()
with driver:
    driver.get('https://go.drugbank.com/pharmaco/metabolomics')  # known url using cloudflare's "under attack mode"

    with open("page_markup_bypass_3.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)