import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get("https://ff.web.sdo.com/web8/index.html#/servers")
server_box = driver.find_element(by=By.CSS_SELECTOR, value='div.serverbox')
servers = server_box.find_elements(by=By.CSS_SELECTOR, value='div.item')
server_map = {}
for server in servers:
    dc_name = server.find_element(by=By.CLASS_NAME, value='itemtit').text
    worlds = server.find_elements(by=By.XPATH, value=".//div[@class='itembox']//div[@class='itline']")
    worlds_name = [x.find_element(by=By.XPATH, value=".//div[@class='lf']//div[@class='name']").text for x in worlds]
    server_map[dc_name] = worlds_name
with open('result.json', 'w', encoding='utf8') as fp:
    json.dump(server_map, fp, ensure_ascii=False)
driver.close()
