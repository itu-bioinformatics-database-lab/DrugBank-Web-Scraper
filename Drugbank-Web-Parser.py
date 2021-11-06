import pandas as pd
from bs4 import BeautifulSoup

def extract_text(soup_obj, tag, attribute_name, attribute_value):
    txt = soup_obj.find(tag, {attribute_name: attribute_value}).text.strip() if soup_obj.find(tag, {attribute_name: attribute_value}) else ''
    return txt

rows = []

for page_number in range(1,125):
    # Change the file location in your device
    with open("pharmaco-metabolomics-data\pharmaco-metabolomics-page{}_markup.html".format(page_number), "r") as file:
        data = file.read()
        soup = BeautifulSoup(data, 'html.parser')
        drug_metabolite_table = soup.find('table', {'class': 'table-metabolite-regulations table table-bordered'})
        drug_metabolite_table_body = soup.find("tbody")
        drug_metabolite_table_body_row = drug_metabolite_table_body.find_all("tr")

        for row in drug_metabolite_table_body_row:
            temp_data = row.find_all("td")
            drug = temp_data[0].text
            metabolite = temp_data[2].text
            change = temp_data[3].text.strip()
            if change == "increased":
                increased = 1
                decreased = 0
            elif change == "decreased":
                decreased = 1
                increased = 0
            else:
                decreased = 0
                increased = 0  
            description = temp_data[4].text
        
            rows.append([drug,metabolite,change,increased,decreased,description])


# Create dataframe and export

columns = ["Drug", "Metabolite", "Change", "Increased", "Decreased", "Description"]

df = pd.DataFrame(data=rows, columns=columns)
df.sort_values(by="Drug", ascending=True, inplace=True)
df.to_csv('pharmaco-metabolomics-data.csv', index=False)
df.to_excel('pharmaco-metabolomics-data.xlsx', index=False)