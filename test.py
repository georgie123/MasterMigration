
import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/Georges/Downloads/tmp_extract_alias_joo_content.xml')
root = tree.getroot()

for my_poi in root.findall('tmp_extract_alias_joo_content'):
    my_title = my_poi.find('title').text
    my_alias = my_poi.find('alias').text
    print(my_title, my_alias)