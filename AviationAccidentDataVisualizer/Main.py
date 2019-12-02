import os
import AviationAccidentDataVisualizer.modules.Preprocess as pre
import AviationAccidentDataVisualizer.modules.DataManagement as dm

import numpy as np
import pandas as pd
if not os.path.isfile('modules/AviationData.csv'):
    file_name = 'AviationData.xml'
    file_path = os.getcwd()
    pre.xml_2csv(file_path,file_name)
df = pd.read_csv('modules/AviationData.csv')
df = pre.drop_nan(df)
print(pd.isna(df['Latitude']).sum(),df.info)
#import geopandas as gp
#import matplotlib.pyplot as plt
#china_geod = gp.GeoDataFrame.from_file('bou2_4p.shp', encoding = 'gb18030')
#china_geod.plot()#查看地图

