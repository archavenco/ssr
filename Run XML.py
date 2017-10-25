import xml.etree.ElementTree as ET
tree = ET.parse('filename.xml') #ดึงไฟล์ data.xml เข้ามา
root = tree.getroot()
home = root.find('home')
print(root.tag)
print(root.attrib)
print(root[0][0].text)
print(root[0][1].text)
print(root)