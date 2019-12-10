"""DataManagement.py
This module contains a function handles column condition querying (single or multiple).
"""
import re
import numpy as np
import pandas as pd


def column_query(df, *cond):
    """This function takes a dataframe and conditions formed as ABC=='abc' or ABC>=10.
    The return value is a dataframe that filtered by given conditions.
    :param df:
    :param cond: list of conditions
    :return: dataframe
    """

    con_lst = []
    for condition in cond:
        index = re.search(r"[<=>]+", condition)
        symbol = index.group()
        span_f = index.span()[0]
        span_s = index.span()[1]
        column_name = condition[:span_f]
        value = condition[span_s:]
        # print(value, type(value))
        if value.isnumeric():
            # con = 'df[' + "\'" + column_name + "\'" + ']' + symbol + value
            con = '(df.' + column_name + symbol + value + ')'
        else:
            # con = 'df[' + "\'" + column_name + "\'" + ']' + symbol + '\''+value+'\''
            con = '(df.' + column_name + symbol + '\'' + value + '\'' + ')'
        con_lst.append(con)
        # print(con)
    new_con = ''
    for i in range(len(con_lst)):
        new_con += con_lst[i]
        if i != len(con_lst) - 1:
            new_con += '&'
        # print(new_con)
    try:
        df = df[eval(new_con)]
    except Exception as e:
        print('Error detail:', e)
        # if df.empty:
        #     raise Exception('No entries satisfies given conditions.')
    assert not df.empty, 'No entries satisfies given conditions.'

    return df


if __name__ == '__main__':
    pass
