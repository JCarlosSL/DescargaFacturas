from xml.etree import ElementTree, ElementInclude
import numpy as np
import zipfile

def lectura(name,name1):
    zf = zipfile.ZipFile(name + '.zip')
    path = zf.open(name1 +'.xml')
    tree = ElementTree.parse(path)
    root = tree.getroot()

    #a = np.array([elem.tag for elem in root.iter()])
    #print(a)

    data =[child.text for child in root.iter('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID')]
    for child in root.iter('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IssueDate'):
        data1=child.text
    return (data1,data[4])
