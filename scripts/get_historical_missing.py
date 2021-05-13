import yfinance as yf
import pandas as pd
from tqdm import tqdm
import os
import time
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./historical_data') if isfile(join('./historical_data', f))]

df = pd.read_csv('./lists/ticker.csv')

for i in tqdm(range(len(df))):
  scrip = df.iloc[i]["TICKER"]
  if scrip in onlyfiles[:-4]:
      continue
  else:
    try:
        temp_df = yf.Ticker(f'{scrip}.NS').history(period='MAX')
        temp_df.dropna(inplace=True)
        temp_df.to_csv(f'./historical_data/{scrip}.csv')
        os.system(f'git add ./historical_data/{scrip}.csv > /dev/null 2>&1 && git commit -m "ADD {scrip} HISTORICAL DATA" > /dev/null 2>&1')
    except:
        time.sleep(30)
        print("SOMETHING WENT WRONG. SWITCH VPN")
        try:
            temp_df = yf.Ticker(f'{scrip}.NS').history(period='MAX')
            temp_df.dropna(inplace=True)
            temp_df.to_csv(f'./historical_data/{scrip}.csv')
            os.system(f'git add ./historical_data/{scrip}.csv > /dev/null 2>&1 && git commit -m "ADD {scrip} HISTORICAL DATA" > /dev/null 2>&1')
        except:
            continue
