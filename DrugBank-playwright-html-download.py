from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()

    for page_number in range(1,125):
        page.goto("https://go.drugbank.com/pharmaco/metabolomics?page={}".format(page_number))
        page.wait_for_timeout(10000)
        # Change the file location in your device
        with open("pharmaco-metabolomics-data\pharmaco-metabolomics-page{}_markup.html".format(page_number), "w", encoding="utf-8") as file:
            file.write(page.content())

    browser.close()