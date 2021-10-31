from selenium import webdriver
from selenium.webdriver.support.ui import Select

chrome_path = 'C:/Users/Georges/PycharmProjects/chromedriver.exe'
browser = webdriver.Chrome(chrome_path)

browser.maximize_window()

browser.get('https://joomla4.master-geomatique.org/administrator/index.php?option=com_content&view=article&layout=edit')

# CONNEXION
username = browser.find_element_by_id('mod-login-username')
password = browser.find_element_by_id('mod-login-password')
username.send_keys('geo854JKOkpJ45carto')
password.send_keys('7yzr7aum§joomla')
browser.find_element_by_id('btn-login-submit').click()

# CHAMPS CLASSIQUE ARTICLE
title = browser.find_element_by_id('jform_title')
alias = browser.find_element_by_id('jform_alias')
txt_src = browser.find_element_by_id('jform_articletext')

title.send_keys('Test article X9')
alias.send_keys('Test-article-X9')
txt_src.send_keys('<p>Paragraphe 1</p>')

# LISTE CATEGORIE
categorie_list = browser.find_element_by_xpath('.//div[@class="choices__inner"][contains(., "Accueil")]')
categorie_list.click()
# Pour choisir News
browser.find_element_by_id('choices--jform_catid-item-choice-8').click()

# LISTE ACCESS
access_list = Select(browser.find_element_by_id('jform_access'))
access_list.select_by_value('8')

# LISTE TAGS
browser.find_element_by_id('jform_tags').click()

# browser.find_element_by_id('save-group-children-save').click()