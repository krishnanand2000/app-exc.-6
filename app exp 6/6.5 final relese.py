import xml.etree.ElementTree as xml1
import xml.dom.minidom as dom
from xml.dom import minidom


def generatexml(merafile):
    root = xml1.Element("users")
    c1 = xml1.Element("person")
    root.append(c1)

    nme = xml1.SubElement(c1,"model")
    nme.text = "innnova"

    address = xml1.SubElement(c1,"model")
    address.text="2018"

    city = xml1.SubElement(c1,"city")
    city.text="varanasi"

    pin = xml1.SubElement(c1,"pincode")
    pin.text="221008"

    ID_no = xml1.SubElement(c1,"reg_no")
    ID_no.text="1001"

    c2 = xml1.Element("person")
    root.append(c2)

    nme = xml1.SubElement(c2,"model")
    nme.text = "ecosport"  

    address = xml1.SubElement(c2,"model")
    address.text="2019"
    
    city = xml1.SubElement(c2,"city")
    city.text="bhagalpur"

    pin = xml1.SubElement(c2,"pincode")
    pin.text="696969"

    ID_no = xml1.SubElement(c2,"reg_no")
    ID_no.text="2001"
    
    tree = xml1.ElementTree(root)
    
    with open (merafile,"wb") as files:
        tree.write(files)

if __name__=="__main__":
        generatexml("customerx.xml")

tree1= xml1.parse("customerx.xml")
root1  = tree1.getroot()
root1.tag

for child in root1:
    print(child.tag, child.attrib)

[elem.tag for elem in root1.iter()]




    


