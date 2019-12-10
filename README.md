# Aviation Accident Data Visualizer

Organization of the Project
---------------------------
```
AviationAccidentDataVisualizer/
  |- aadv/
     |- modules/
        |- data/
           |- AviationData.xml
        |- __init__.py
        |- preprocess.py
        |- data_management.py
        |- test_data_management.py
        |- test_preprocess.py 
     |- __init__.py
  |- examples/
     |- examples.ipynb
  |- docs/
     |-Component Specification.txt
     |-Functional Specification.txt
  |- LICENSE
  |- README.md
  |- setup.py
  |- requirements.txt
  |- .travis.yml
  |- .gitignore
```
  
  
  Installation
------------
To install, you will need to begin by cloning `AviationAccidentDataVisualizer` on your own computer by using the following `git` command:

```
git clone https://github.com/TianyiZhang0315/AviationAccidentDataVisualizer
```

Next, to install the package you will need to go into the `AviationAccidentDataVisualizer` directory and run the `setup.py` file:

```
cd AviationAccidentDataVisualizer/
python setup.py install
```

To ensure that the dependencies to run `AviationAccidentDataVisualizer` are installed on your computer you will want to run the following command:

```
pip install -r requirements.txt
```

## Background
Aviation safety is always an important
research area in transportation safety.
Although aviation accident is one of the rarest transportation accidents, the fatal rate of aviation accident is among the highest.
Causes of aviation accidents are extremely complicated and unpredictable.
In last 2 years, Boeing 737 MAX has suffered 2 hull loss accidents, including Lion Air Flight 610 crash in 2018, and Ethiopian Airlines Flight 302 crash in 2019. We hope this project can give people  some intuitive feelings about aviation accidents in U.S., and arouse our awareness of aviation safety as well.

## Project Overview
This project is intended to create a tool for users who are interested in aviation accident in U.S.. The basic functions of this package are data query and map visualization, which can be accomplished with pandas and folium in Python.
The data we use is from DATA.GOV. It is named Aviation Data and Documentation from the NTSB Accident Database System and released by National Transportation Safety Board.

## Python library
1) Folium: Folium is used to visualize aviation data across the US specified by accident location. Several location correlated inquiries can be easily visualized by adding corresponding layers on top of it, such as terrain, weather, etc..
2) Matplotlib: Matplotlib is a powerful tool to use for analyzing relationships between each aspects of an accident, such as month/date of the year, tendency of number of accidents in past decades, location of the accident and aircraft manufacturer and model. 
3) Pandas: A dataframe of this aviation accident data could be created by Pandas, which is relatively efficient while easy to use. Users can query different columns, or look up certain aviation accident by several key properties, such as number of injuries or death, accident date or type, aircraft make or model.

## Data link
https://drive.google.com/open?id=17jI7E2Q-nf9uggiiyDfyJnbZaaa1ekJ-
