
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import pandas as pd
path = ''

def xml_2csv(input_path, file_name):
    tree = ET.ElementTree(file=input_path+'\\'+file_name)
    root = tree.getroot()
    print(root.tag, root.attrib)
    lst = []
    i = 0
    for elem in tree.iter():
        if i == 2:
            print(elem.attrib)
        lst.append(elem.attrib)
        i += 1
    lst = lst[2:]
    keys = list(lst[0].keys())
    df = pd.DataFrame.from_dict(lst)
    df.to_csv(input_path+'\\'+'AviationData.csv', index=None, header=True)
    return
def drop_nan(df):

    return df.dropna(subset = ['Longitude','Latitude'])
