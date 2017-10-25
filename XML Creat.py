import xml.etree.cElementTree as ET


root = ET.Element("root")
ET.SubElement(root, 'Count').text = '7'
doc = ET.SubElement(root, "results")


ET.SubElement(doc, 'id').text = '1'
ET.SubElement(doc, "First_Name").text = "Sirawich"
ET.SubElement(doc, "Last_Name").text = "Songsaeng"

tree = ET.ElementTree(root)
tree.write("filename.xml")