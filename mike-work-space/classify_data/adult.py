import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import requests
import json
from base64 import urlsafe_b64encode

def retrive_all_urls():
    files = glob.glob('data-to-use/*.csv')
    df_2020 = pd.DataFrame(columns= pd.read_csv(files[0]).columns)
    for f in files:
        df = pd.read_csv(f)
        df_2020 = df_2020.append(df[(df.years == 2020)],ignore_index= True)
    df = df_2020[(df_2020['query'].notna())]
    urls = []
    for index, row in df.iterrows():
        if ".com" in row.query.lower(): #add conditionals add needed to this if statement to narrow results
            url = [i for i in row.query.lower().split(" ") if ".com" in i][0].strip().split(".com")[0]+".com".lower()#.split(".")[-1].lower().split("/")[-1]
            url_clean = url.replace("https://","").replace("http://","").replace("www.","")
            if url_clean not in urls: 
                urls.append(url_clean)
    return urls

def call_api(target_website):
    target_website = target_website.encode()
    key = "5pa0Zw9Pyb9a5d7jee2A"
    secret_key = "xj3uOlocAPp004ZMraUx"
    while True:
        try:
            api_url = "https://api.webshrinker.com/categories/v3/%s" % urlsafe_b64encode(target_website).decode('utf-8')
            response = requests.get(api_url, auth=(key, secret_key))
            status_code = response.status_code
            data = response.json()
            if status_code == 200:
                category_data = data['data'][0]['categories']
                return category_data
            elif status_code == 202:
                return None
            else:
                print("An error occurred: HTTP %d" % status_code)
                if 'error' in data:
                    print(data['error']['message'])
        except Exception:
            continue
        break


df = pd.read_csv("cook.csv")
urls = retrive_all_urls()
for url in urls:
    data = call_api(url)
    new_row = {"url":url,"classification":data}
    df = df.append(new_row, ignore_index=True)
    df.to_csv("cook.csv",index=False)
    if data == None:    
        print("Url NOT Classified")
    else:
        print("Url Classified")
       