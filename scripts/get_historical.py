import yfinance as yf
import pandas as pd
import tqdm
import os
df = pd.read_csv('./lists/ticker.csv')

for i in tqdm(range(len(df))):
  scrip = df.iloc[i]["TICKER"]
  temp_df = yf.Ticker(f'{scrip}.NS').history(period='MAX')
  temp_df.dropna(inplace=True)
  temp_df.to_csv(f'./historical_data/{scrip}.csv')
  os.system(f'git add ./historical_data/{scrip}.csv > /dev/null 2>&1 && git commit -m "ADD {scrip} HISTORICAL DATA" > /dev/null 2>&1 && git push > /dev/null 2>&1')
