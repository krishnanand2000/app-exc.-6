import xml.etree.ElementTree as xml
from xml.dom import minidom


def generatexml(myfile):
    root = xml.Element("users")
    c1 = xml.Element("person")
    root.append(c1)

    nme = xml.SubElement(c1,"name")
    nme.text = "krishnanand"

    address = xml.SubElement(c1,"address")
    address.text="ramnagar"

    city = xml.SubElement(c1,"city")
    city.text="varanasi"

    pin = xml.SubElement(c1,"pincode")
    pin.text="221008"

    ID_no = xml.SubElement(c1,"ID_no")
    ID_no.text="1001"

    c2 = xml.Element("person")
    root.append(c2)

    nme = xml.SubElement(c2,"name")
    nme.text = "arunish"  

    address = xml.SubElement(c2,"address")
    address.text="bihar"
    
    city = xml.SubElement(c2,"city")
    city.text="bhagalpur"

    pin = xml.SubElement(c2,"pincode")
    pin.text="696969"

    ID_no = xml.SubElement(c2,"ID_no")
    ID_no.text="2001"

    c3 = xml.Element("person")
    root.append(c3)

    nme = xml.SubElement(c3,"name")
    nme.text = "shibin"

    address = xml.SubElement(c3,"address")
    address.text="kerla"

    city = xml.SubElement(c3,"city")
    city.text="kochin"

    pin = xml.SubElement(c3,"pincode")
    pin.text="221099"

    ID_no = xml.SubElement(c3,"ID_no")
    ID_no.text="3001"

    c4 = xml.Element("person")
    root.append(c4)

    nme = xml.SubElement(c4,"name")
    nme.text = "aashish"


    address = xml.SubElement(c4,"address")
    address.text="mohali"

    city = xml.SubElement(c4,"city")
    city.text="chandigarh"

    pin = xml.SubElement(c4,"pincode")
    pin.text="221005"

    ID_no = xml.SubElement(c4,"ID_no")
    ID_no.text="4001"

    tree = xml.ElementTree(root) 

    with open (myfile,"wb") as files:
        tree.write(files)

if __name__=="__main__":
    generatexml("customer4.xml")

doc = minidom.parse("customer4.xml")
name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)
persons = doc.getElementsByTagName("person")
for person in persons:
        
        name = person.getElementsByTagName("name")[0]
        address = person.getElementsByTagName("address")[0]
        city = person.getElementsByTagName("city")[0]
        pincode = person.getElementsByTagName("pincode")[0]
        ID_no = person.getElementsByTagName("ID_no")[0]
        print("name:%s, address:%s, city:%s, pincode:%s ,ID_no:%s" %
              ( name.firstChild.data, address.firstChild.data, city.firstChild.data,pincode.firstChild.data , ID_no.firstChild.data))



