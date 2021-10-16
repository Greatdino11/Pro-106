import pandas as pd
import plotly.express as px
import numpy as np
import csv

def get_data(file_name):
    coffee = []
    sleep = []
    with open(file_name) as o_file:
        file = csv.DictReader(o_file)
        
        for i in file:
            coffee.append(float(i['Coffee in ml']))
            sleep.append(float(i['sleep in hours']))
        
    return{'x': coffee, 'y': sleep}

def find_cor(data):
    cor = np.corrcoef(data['x'], data['y'])
    print(cor[0, 1])

def setup():
    file_name = 'coffee.csv'
    data = get_data(file_name)
    find_cor(data)

setup()