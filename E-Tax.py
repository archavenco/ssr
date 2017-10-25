import xml.etree.ElementTree as ET
tree = ET.parse('filename.xml') #ดึงไฟล์ data.xml เข้ามา
root = tree.getroot()

print(root)
