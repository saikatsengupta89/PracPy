from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re
from azure.storage.filedatalake import DataLakeServiceClient


def initialize_storage_account(storage_account_name, storage_account_key):
    try:
        global service_client
        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)
        #print(service_client)
    except Exception as e:
        print(e)


def list_directory_contents():
    try:
        file_system_client = service_client.get_file_system_client(file_system="adsazuksdevedwcontainer")
        paths = file_system_client.get_paths(path="RDH")
        for path in paths:
            print(path.name + '\n')

    except Exception as e:
        print(e)

def upload_file_to_directory():
    try:
        file_system_client = service_client.get_file_system_client(file_system="adsazuksdevedwcontainer")
        directory_client = file_system_client.get_directory_client("Sandbox/POC/RawData/test/2021/04/15")
        file_client = directory_client.create_file("exchange_rates.csv")

        local_file = open("C:\\Users\\sss.it\\PycharmProjects\\GetFXRates\\ExchangeRate.csv",'r')
        file_contents = local_file.read()

        file_client.append_data(data=file_contents, offset=0, length=len(file_contents))
        file_client.flush_data(len(file_contents))

    except Exception as e:
        print(e)

if __name__ =="__main__":
    url = "https://www.centralbank.ae/en/fx-rates"
    storage_account_name="adsazuksdevdatalake"
    storage_account_key ="G6Ndtzsa4N4ld8GtaTCcSYYIGEreudtmDABE+o90FnZqOlJSD1ZehD5Xib5J0BeEoCLiq4a/+kP0i5hdTdpBrw=="

    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    print(type(soup))

    # Print out the text
    text = soup.get_text()

    # Print the first 10 rows for sanity check
    rows = soup.find_all('tr')
    for row in rows:
        row_td = row.find_all('td')
        str_cells = str(row_td)
        cleantext = BeautifulSoup(str_cells, "lxml").get_text()
        # print(cleantext)

    country_code = []
    exchange_rate = []

    for row in rows:
        cells = row.find_all('td')
        str_cells = str(cells)
        clean = re.compile('<.*?>')
        clean2 = (re.sub(clean, '', str_cells))
        clean3 = clean2.replace('[', '').replace(']', '')
        clean4 = clean3.split(',')
        if clean4[0] != '':
            country_code.append(clean4[0])
        if clean4[-1] != '':
            exchange_rate.append(clean4[-1])

    ratesDF = pd.DataFrame(list(zip(country_code, exchange_rate)), columns=['country_code', 'exchange_rate'])
    ratesDF.to_csv("ExchangeRate.csv",index=False)
    print(ratesDF)

    initialize_storage_account (storage_account_name, storage_account_key)
    upload_file_to_directory ()
