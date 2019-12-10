"""test_Preprocess.py
This file is a test file for Preprocess module.

"""
import modules.preprocess as pre
import os

PATH = os.path.dirname(os.path.abspath(__file__))
if __name__ == '__main__':
    # one-shot test for xml_2csv()
    print('one-shot test for xml_2csv()')
    try:
        pre.xml_2csv(PATH, 'AviationData.xml')
        print('Successfully run sml_2csv().')
    except Exception as e:
        print(e)

    # one-shot test for dataset()
    print('one-shot test for dataset()')
    try:
        df = pre.dataset()
        print('Successfully run sml_2csv().')
    except Exception as e:
        print(e)
