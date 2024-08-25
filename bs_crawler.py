import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
# options.binary_location = '/usr/bin/chromium-browser'
options.add_argument('--headless')  # Roda o Chrome em modo headless (sem interface gráfica)
options.add_argument('--disable-dev-shm-usage')  # Evita problemas com uso de memória compartilhada
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')  # Define um user-agent
# options.add_argument('--disable-gpu')  # Desativa o uso de GPU (não é necessário em headless)
options.add_argument('--window-size=1920x1080')  # Define o tamanho da janela (ajuda na renderização)
options.add_argument('--disable-software-rasterizer')  # Desativa rasterização de software

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
# driver = webdriver.Chrome(service='C:\\Users\\daisy\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe', options=options)
# wait = WebDriverWait(driver, 30)


url = 'https://mac.com.br/empreendimentos/'

driver.get(url)

# Esperar o carregamento completo da página
driver.implicitly_wait(10)


# Identificar o iframe e alternar para ele
iframe = driver.find_element("iframe", "iframe")  # Encontre o iframe pelo tag name, id, etc.
driver.switch_to.frame(iframe)


# Agora, o HTML completo pode ser extraído
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')



items = []
empreendimentos = soup.find_all('article', class_='mac__enterprises-items--item--infos')
caracteristicas = soup.find_all('div', class_='mac__enterprises-items--item--wrapper--items')

for item in empreendimentos:
    nome_do_empreendimento = item.find('h3', class_='mac__enterprises-name').text
    if soup.find('span', class_='mac__icon is--dorms'):
        metragem = item.find('p', class_='mac__enterprises-text').text
        
    items.append([nome_do_empreendimento, metragem])
    # items.append({'Nome': nome_do_empreendimento, 'Metragem': metragem})

for item_1 in caracteristicas:
  if soup.find('span', class_='mac__icon is--dorms'):
      metragem = item_1.find('p', class_='mac__enterprises-text').text
      endereco = item_1.find('p', class_='mac__enterprises-text').text
      bairro = item_1.find('p', class_='mac__enterprises-text').text
      status = item_1.find('p', class_='mac__enterprises-text').text

      items.append([metragem, endereco, bairro, status])

    #   items.append({'Metragem': metragem, 'Endereço': endereco, 
    #                 'Bairro': bairro, 'Status do Projeto': status})

# # Criando o DataFrame
# df = pd.DataFrame(items)


driver.switch_to.default_content()

# Fechar o navegador
driver.quit()

# # Analisar o HTML usando BeautifulSoup
# soup = BeautifulSoup(page_source, 'html.parser')


# items = []
# empreendimentos = soup.find_all('article', class_='mac__enterprises-items--item--infos')
# caracteristicas = soup.find_all('div', class_='mac__enterprises-items--item--wrapper--items')

# for item in empreendimentos:
#     nome_do_empreendimento = item.find('h3', class_='mac__enterprises-name').text
#     if soup.find('span', class_='mac__icon is--dorms'):
#         metragem = item.find('p', class_='mac__enterprises-text').text
        
#     items.append([nome_do_empreendimento, metragem])
#     # items.append({'Nome': nome_do_empreendimento, 'Metragem': metragem})

# for item_1 in caracteristicas:
#   if soup.find('span', class_='mac__icon is--dorms'):
#       metragem = item_1.find('p', class_='mac__enterprises-text').text
#       endereco = item_1.find('p', class_='mac__enterprises-text').text
#       bairro = item_1.find('p', class_='mac__enterprises-text').text
#       status = item_1.find('p', class_='mac__enterprises-text').text

#       items.append([metragem, endereco, bairro, status])

#     #   items.append({'Metragem': metragem, 'Endereço': endereco, 
#     #                 'Bairro': bairro, 'Status do Projeto': status})

# # Criando o DataFrame
# df = pd.DataFrame(items)


# Criar o DataFrame
df = pd.DataFrame(items, columns=['Empreendimento', 'Dorms', 'Endereço', 'Bairro', 'Status'])

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dados_corrigidos.csv', index=False, encoding='utf-8')

print("Dados extraídos e salvos com sucesso!")