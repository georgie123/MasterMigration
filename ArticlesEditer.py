from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

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
    xml_title = xml_title.replace('  ', ' ')

    if xml_title != 'Test georges' \
            and xml_title != 'Test cours m2 georges' \
            and xml_title != 'Test georges4' \
            and xml_title != 'Logo (New)' \
            and xml_title != 'Présentation générale' \
            and xml_title != 'Options d&apos;édition' \
            and xml_title != 'Options d\'édition' \
            and xml_title != 'Précisions' \
            and xml_title != 'Bienvenue' \
            and xml_title != 'IMG1' \
            and xml_title != 'IMG2' \
            and xml_title != 'IMG3' \
            and xml_title != 'Présentation Actualités' \
            and xml_title != 'Présentation Actualités 2' \
            and xml_title != 'Master Géomatique' \
            and xml_title != 'Expertise numérique et territoriale' \
            and xml_title != 'Formation en alternance' \
            and xml_title != 'XXXXXXXXX':

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