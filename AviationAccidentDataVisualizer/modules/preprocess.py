"""Preprocess.py
This module takes AviationData.xml and provides a series of function
for data cleaning and preprocessing."""
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import pandas as pd
import os

PATH = os.path.dirname(os.path.abspath(__file__))
FILENAME = 'AviationData.xml'


def xml_2csv(input_path, file_name):
    """
    This function reads the xml data file and save it as csv file into given directory.
    :param input_path:
    :param file_name:
    :return: None
    """
    tree = ET.ElementTree(file=input_path + '\\' + file_name)
    root = tree.getroot()
    # print(root.tag, root.attrib)
    lst = []
    i = 0
    for elem in tree.iter():
        # if i == 2:
        # print(elem.attrib)
        lst.append(elem.attrib)
        i += 1
    lst = lst[2:]
    # keys = list(lst[0].keys())
    df = pd.DataFrame.from_dict(lst)
    df.to_csv(input_path + '\\' + 'AviationData.csv', index=None, header=True)
    return


"""Now do drop nan in visualizer"""


# def drop_nan(df):
#     """This function drop all entries that contains NaN values.
#     :param df:
#     :return:dataframe
#     """
#     return df.dropna(subset = ['Longitude','Latitude'])


def elim_country(df):
    """This function returns a dataframe that only contains entries if 'Country' == 'United States'.
    :param df:
    :return:dataframe
    """
    return df[df['Country'] == 'United States']


def create_state(df):
    """This function creates a new column 'State' for the dataframe.
    :param df:
    :return: dataframe
    """
    df['State'] = [str(x)[-2:] for x in df['Location'].values]
    return df


def dataset():
    """This function is the main function of this module. Users should import this module and call this
    function to obtain the clean dataframe of AviationData.xml for querying and visualization.
    :param path:
    :return: dataframe
    """
    global FILENAME, PATH

    if not os.path.isfile(PATH + '\\' + 'AviationData.csv'):
        xml_2csv(PATH, FILENAME)
    df = pd.read_csv(PATH + '\\' + 'AviationData.csv')
    # df = drop_nan(df)
    df = elim_country(df)
    df = create_state(df)
    return df


if __name__ == '__main__':
    df = dataset()
    print(df.info)
