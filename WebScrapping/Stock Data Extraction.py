!pip install yfinance==0.2.4
!pip install pandas==1.3.3

import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")

!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json

# Extracting Stock info as a dictionary
import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info

apple_info['country']

# Share price of the stock over a certain period of time
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")
apple.dividends
appl.dividends.plot()

# Advanced Micro Devices
amd = yf.Ticker("AMD")
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json

import json
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
amd_info

# Exercise
amd_share_info = amd.history(period="max")
amd_share_info.head(1)
amd_share_info.iloc[0][4]
amd_info['country']
amd_info['sector']
