#This file contains use examples for Aviation Accident Data Visualizer package
#import preprocess and DataManagement modules
import os
os.chdir(os.path.dirname(os.path.abspath('')))
import aadv.modules.Preprocess as pre
import aadv.modules.Data_Management as dm
import aadv.modules.Visualizer as vis
import pandas as pd

#obtain cleaned dataframe
df = pre.dataset()

#setting condtions, compared with either string or int.
q = 'State==AK'
p = 'TotalUninjured>=2'

#call query function in DataManagement module and return a dataframe
df = dm.column_query(df, q,p)

#check conditioned columns
#print(df[['State','TotalUninjured']])

#heatmap visualization
vis.time_ranged_heat_map(df)
