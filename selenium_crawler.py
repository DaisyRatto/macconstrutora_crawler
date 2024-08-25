from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# site MSC cruzeiros. Próximo projeto
# website = "https://www.msccruzeiros.com.br/Search%20Result?area=SOA&passengers=2%7C0%7C0%7C0&departureDateFrom=23%2F08%2F2024&departureDateTo=22%2F08%2F2027&page=1"

website = "https://mac.com.br/empreendimentos"
path = r"C:\Users\daisy\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=path)
# options = Options()
# options.add_argument('--headless')

driver = webdriver.Chrome(service=service)
driver.get(website)

time.sleep(30)


articles = driver.find_elements(by="xpath", value='//article[@class="mac__enterprises-items--item--infos"]')

project_names = []
addresses = []
neighborhoods = []
footages = []
statuses = []

for article in articles:
    project_name = article.find_element(by="xpath", value='./h2').text
    endereco = article.find_element(by="xpath", value='./div/div/p').text
    bairro = article.find_element(by="xpath", value='./div/div/p').text
    metragem = article.find_element(by="xpath", value='./div/div/p').text
    status = article.find_element(by="xpath", value='./div/div/p').text

    project_names.append(project_name)
    addresses.append(endereco)
    neighborhoods.append(bairro)
    footages.append(metragem)
    statuses.append(status)

driver.quit()

df = pd.DataFrame({
    'Project Name': project_names,
    'Address': addresses,
    'Neighborhood': neighborhoods,
    'Footage': footages,
    'Project Phase': statuses
})

df.to_csv('headlines.csv')