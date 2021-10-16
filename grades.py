import pandas as pd
import plotly.express as px
import numpy as np
import csv

def get_data(file_name):
    grades = []
    days = []
    with open(file_name) as o_file:
        file = csv.DictReader(o_file)
        
        for i in file:
            grades.append(float(i['Marks In Percentage']))
            days.append(float(i['Days Present']))
        
    return{'x': grades, 'y': days}

def find_cor(data):
    cor = np.corrcoef(data['x'], data['y'])
    print(cor[0, 1])

def setup():
    file_name = 'grades.csv'
    data = get_data(file_name)
    find_cor(data)

setup()