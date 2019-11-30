
import re
import numpy as np
import pandas as pd
def column_query(df, *cond):
    result = []
    for condition in cond:
        index = re.search(r"[<=>]+", condition)
        symbol = index.group()
        span_f = index.span()[0]
        span_s = index.span()[1]
        column_name = condition[:span_f]
        value = condition[span_s:]
        con = 'df['+"'"+column_name+"'"+']'+symbol+ value
        result.append(df[eval(con)])
    return result
# df = pd.DataFrame(np.array([[1, 2, 3], [4, 5,np.nan], [7, 8, 9]]),
#                    columns=['a', 'b', 'c'])
# print(pd.isna(df['c']))

