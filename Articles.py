from selenium import webdriver
import time
import xml.etree.ElementTree as ET

chrome_path = 'C:/Users/Georges/PycharmProjects/chromedriver.exe'
browser = webdriver.Chrome(chrome_path)

tree = ET.parse('C:/Users/Georges/Downloads/Tmp_extract_alias_joo_content.xml')
root = tree.getroot()

browser.maximize_window()
browser.get('https://joomla4.master-geomatique.org/administrator/index.php?option=com_content&view=article&layout=edit')

# CONNEXION
username = browser.find_element_by_id('mod-login-username')
password = browser.find_element_by_id('mod-login-password')
username.send_keys('geo854JKOkpJ45carto')
password.send_keys('7yzr7aum§joomla')
browser.find_element_by_id('btn-login-submit').click()

for my_poi in root.findall('Tmp_extract_alias_joo_content'):
    xml_title = my_poi.find('title').text
    xml_alias = my_poi.find('alias').text

    browser.maximize_window()
    browser.get('https://joomla4.master-geomatique.org/administrator/index.php?option=com_content&view=article&layout=edit')

    # CHAMPS CLASSIQUE ARTICLE
    title = browser.find_element_by_id('jform_title')
    alias = browser.find_element_by_id('jform_alias')

    title.send_keys(xml_title)
    alias.send_keys(xml_alias)

    browser.find_element_by_id('save-group-children-save').click()

    time.sleep(2)