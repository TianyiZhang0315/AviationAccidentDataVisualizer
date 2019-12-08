"""test_Preprocess.py
This file is a test file for Preprocess module.

"""
import Preprocess as pre
import os
if __name__ == '__main__':
    #one-shot test for xml_2csv()
    print('one-shot test for xml_2csv()')
    try:
        pre.xml_2csv(os.getcwd(),'AviationData.xml')
        print('Successfully run sml_2csv().')
    except Exception as e:
        print(e)


    #one-shot test for dataset()
    print('one-shot test for dataset()')
    try:
        df = pre.dataset(os.getcwd())
        print('Successfully run sml_2csv().')
    except Exception as e:
        print(e)

