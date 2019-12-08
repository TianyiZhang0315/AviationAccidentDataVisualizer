"""test_DataManagement.py
This file is a test file for DataManagement module.
"""
import DataManagement as dm
import pandas as pd
import numpy as np
if __name__ == '__main__':

    # Edge test for column_query() to trigger no column exception in function
    print('Edge test 1 for column_query()')
    df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns = ['a', 'b', 'c'])
    condition_1 = 'State==AK'
    condition_2 = 'Latitude<=20'
    try:
        df = dm.column_query(df,condition_1,condition_2)
        print('Exception triggered.')
    except Exception as e:
        print(e)

    # Edge test for column_query() to trigger no entries exception in function
    print('Edge test 2 for column_query()')
    df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
    condition_3 = 'a>=10'
    try:
        df = dm.column_query(df,condition_3)
    except Exception as e:
        print(e)
        print('Exception triggered.')