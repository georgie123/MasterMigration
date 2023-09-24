from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

chrome_path = 'C:/Users/Georges/PycharmProjects/chromedriver.exe'
browser = webdriver.Chrome(chrome_path)

tree = ET.parse('C:/Users/Georges/Downloads/Tmp_extract_alias_joo_content.xml')
root = tree.getroot()

browser.maximize_window()
browser.get('https://j4binv.master-geomatique.org/administrator/index.php?option=com_content&view=articles')

# CONNEXION
username = browser.find_element("id", "mod-login-username")
password = browser.find_element("id", "mod-login-password")
username.send_keys('geo854JKOkpJ45carto')
password.send_keys('7yzr7aum§joomla')
browser.find_element("id", "btn-login-submit").click()

browser.get('https://j4binv.master-geomatique.org/administrator/index.php?option=com_content&view=articles')
time.sleep(1)
browser.find_element("id", "list_limit").click()
time.sleep(1)
browser.find_element("xpath", "//select/option[@value='0']").click()

for my_poi in root.findall('Tmp_extract_alias_joo_content'):
    xml_title = my_poi.find('title').text

    print(xml_title)
    # browser.maximize_window()


    # browser.find_element("xpath", "//a[@href='/administrator/index.php?option=com_content&task=article.edit&id=1']").click()

    # browser.find_element(By.LINK_TEXT, "Présentation générale").click()

    element = browser.find_element(By.LINK_TEXT, xml_title)
    time.sleep(1)
    browser.execute_script("arguments[0].click();", element)
    time.sleep(1)
    browser.find_element("id", "save-group-children-save").click()

    time.sleep(1)