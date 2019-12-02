import os
os.chdir('C:/Users/ALLEN/Desktop/UWSEDS/CSE583_Project/modules')
import Preprocess as pre
import DataManagement as dm

import numpy as np
import pandas as pd
if not os.path.isfile('AviationData.csv'):
    file_name = 'AviationData.xml'
    file_path = os.getcwd()
    pre.xml_2csv(file_path,file_name)
df = pd.read_csv('AviationData.csv')
from matplotlib import pyplot as plt
import seaborn as sns
nan = pd.isna(df).sum()
nan1 = pd.DataFrame()
nan1['Columns'] = [i for i in range(len(nan.index))]
nan1['NaN_count'] = nan.values
country = df['Country'].value_counts()
nan = nan.to_frame()
print(nan)

sns.barplot(x = 'Columns', y = 'NaN_count', data=nan1).set_title('NaN Value Count')
sns.pie()
#plt.figure(1)
#plt.title('NaN Value Count in Features')
#plt.bar([i for i in range(len(nan.keys()))],nan.values)
#plt.figure(2)
#plt.title('Country Distribution')
#labels = ['United States','Other']
#sum_c = df[df['Country'] != 'United States'].count()
#sum_u = df[df['Country'] == 'United States'].count()
#size = [sum_u['Country'], sum_c['Country']]
#plt.pie(size, labels = labels,autopct = '%3.2f%%',
#                      shadow = True,)
df = pre.drop_nan(df)
print(country.keys())
df = pre.elim_country(df)
df.to_csv('AviationDataN.csv', index=None, header=True)
print(pd.isna(df['Latitude']).sum(),df.info)
print(df['Country'].value_counts())
states = df['Location'].values