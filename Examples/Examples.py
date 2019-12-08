#This file contains use examples for Aviation Accident Data Visualizer package
#import preprocess and DataManagement modules
import AviationAccidentDataVisualizer.modules.Preprocess as pre
import AviationAccidentDataVisualizer.modules.DataManagement as dm
import pandas as pd

#obtain cleaned dataframe
df = am.dataset()

#setting condtions, compared with either string or int.
q = 'State==AK'
p = 'TotalUninjured>=2'

#call query function in DataManagement module and return a dataframe
df = dm.column_query(df, q,p)

#check conditioned columns
#print(df[['State','TotalUninjured']])
