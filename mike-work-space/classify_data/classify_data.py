import glob
import ast
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import requests
import json
from base64 import urlsafe_b64encode


def retrive_classified_df():
    df = pd.read_csv("url_classified.csv")
    return convert_dict(df.set_index('url')['classification'].to_dict())

def convert_dict(dict):
    for key in dict.keys():
        categories = []
        if str(dict[key]) != "nan":
            raw_cats = ast.literal_eval(dict[key])
        else: 
            raw_cats = []
        for category in raw_cats:  
            temp_array = [category['label'],category['score']]
            categories.append(temp_array)
        dict[key.strip()] = categories
    return dict

def add_new_column(df,key_dict):
    categories_shrinker_api = []
    for index, row in df.iterrows():
        keyFound = False
        for key in key_dict.keys():
            if key.lower() in str(row['query']).lower():
                categories_shrinker_api.append(key_dict[key])
                keyFound = True
                break
        if keyFound == False:
            categories_shrinker_api.append("N/A")
    print(df.shape[0])
    print(len(categories_shrinker_api))
    print("User Converted")
    df["categories_shrinker_api"] = categories_shrinker_api
    return df



def retrieve_users():
    key_dict = retrive_classified_df()
    files = glob.glob('data-to-use/*.csv')
    for f in files:
        df = pd.read_csv(f)
        df = add_new_column(df,key_dict)
        df.to_csv("data-test-new/"+str(f).split('/')[1])                
retrieve_users()   
