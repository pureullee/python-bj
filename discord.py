import requests
import pandas as pd
from datetime import time, datetime


url = "https://discord.com/api/webhooks/1107664885963313152/Q0OWo9nNMqQynukLyDR4SpBIH7SunN_TxXnZA5WYN60VdgLY2ULOC0gmYdjEyMEruYuA"
bossTime = "./bosstime.xlsx"

df = pd.read_excel(bossTime)

print(df['출현시간'].dtype)
df.set_index('출현시간',inplace=True)
df.columns =[x for x in range(0,7)]

headers = {
    'Content-Type' : 'application/json',
}
msg ="msg"
data = {
  "content": msg
}

if datetime.today()-datetime.combine(datetime.today(),df.index[0]

  



  

  




#r = requests.post(url, json=data, headers=headers)
