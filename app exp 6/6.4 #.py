import xml.etree.ElementTree as xml1
import xml.dom.minidom as dom
from xml.dom import minidom


def generatexml(merafile):
    root = xml1.Element("users")
    c1 = xml1.Element("person")
    root.append(c1)

    nme = xml1.SubElement(c1,"name")
    nme.text = "krishnanand"

    address = xml1.SubElement(c1,"address")
    address.text="ramnagar"

    city = xml1.SubElement(c1,"city")
    city.text="varanasi"

    pin = xml1.SubElement(c1,"pincode")
    pin.text="221008"

    ID_no = xml1.SubElement(c1,"ID_no")
    ID_no.text="1001"

    c2 = xml1.Element("person")
    root.append(c2)

    nme = xml1.SubElement(c2,"name")
    nme.text = "arunish"  

    address = xml1.SubElement(c2,"address")
    address.text="bihar"
    
    city = xml1.SubElement(c2,"city")
    city.text="bhagalpur"

    pin = xml1.SubElement(c2,"pincode")
    pin.text="696969"

    ID_no = xml1.SubElement(c2,"ID_no")
    ID_no.text="2001"
    
    tree = xml1.ElementTree(root) 

    with open (merafile,"wb") as files:
        tree.write(files)

if __name__=="__main__":
    generatexml("customer.xml")

doc = dom.parse("customer.xml")
print(doc.nodeName)
print(doc.firstChild.tagName)

#creating a new xml tag and add it to the document

newexpertise = doc.createElement("expertise")
newexpertise.setAttribute("name" , "Bigdata")
doc.firstChild.appendChild(newexpertise)
print(" ")

expertise = doc.getElementsByTagName("expertise")
print("%d expertise:" % expertise.length )
for skill in expertise:
    print(skill.getAttribute("name"))
    

expertise = doc.getElementsByTagName("expertise")
print("%d List_of_tags" % expertise.length)
for skill in expertise:
    print(skill.getAttribute("name"))







