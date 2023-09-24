from selenium import webdriver
import time
import xml.etree.ElementTree as ET

chrome_path = 'C:/Users/Georges/PycharmProjects/chromedriver.exe'
browser = webdriver.Chrome(chrome_path)

tree = ET.parse('C:/Users/Georges/Downloads/Tmp_extract_alias_joo_content.xml')
root = tree.getroot()

browser.maximize_window()
browser.get('https://j4binv.master-geomatique.org/administrator/index.php?option=com_content&view=article&layout=edit')

# CONNEXION
username = browser.find_element("id", "mod-login-username")
password = browser.find_element("id", "mod-login-password")
username.send_keys('geo854JKOkpJ45carto')
password.send_keys('7yzr7aum§joomla')
browser.find_element("id", "btn-login-submit").click()

for my_poi in root.findall('Tmp_extract_alias_joo_content'):
    xml_title = my_poi.find('title').text
    xml_alias = my_poi.find('alias').text

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
        # browser.get('https://joomla4.master-geomatique.org/administrator/index.php?option=com_content&view=article&layout=edit')
        browser.get('https://j4binv.master-geomatique.org/administrator/index.php?option=com_content&view=article&layout=edit')

        # CHAMPS CLASSIQUE ARTICLE
        title = browser.find_element("id", "jform_title")
        alias = browser.find_element("id", "jform_alias")

        title.send_keys(xml_title)
        alias.send_keys(xml_alias)

        browser.find_element("id", "save-group-children-save").click()

        time.sleep(1)