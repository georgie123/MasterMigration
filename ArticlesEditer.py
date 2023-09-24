from selenium import webdriver
import time
import xml.etree.ElementTree as ET

chrome_path = 'C:/Users/Georges/PycharmProjects/chromedriver.exe'
browser = webdriver.Chrome(chrome_path)

liste_des_id_nouveau_site = [1,2,3,4,5]

browser.maximize_window()
browser.get('https://j4binv.master-geomatique.org/administrator/index.php?option=com_content&view=articles')

# CONNEXION
username = browser.find_element("id", "mod-login-username")
password = browser.find_element("id", "mod-login-password")
username.send_keys('geo854JKOkpJ45carto')
password.send_keys('7yzr7aum§joomla')
browser.find_element("id", "btn-login-submit").click()

for i in liste_des_id_nouveau_site:

    # browser.maximize_window()
    browser.get('https://j4binv.master-geomatique.org/administrator/index.php?option=com_content&view=article&layout=edit&id=' + i)

    browser.find_element("id", "save-group-children-save").click()

    time.sleep(1)