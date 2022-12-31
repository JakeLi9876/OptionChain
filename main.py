import yfinance as yf
import pandas as pd
from FinanceData import FinanceData
from pathlib import PureWindowsPath
from datetime import datetime

ticker = "SPY"
filePath = r"C:\Python\spyOptionData.xlsx"
droppedColumnName = "lastTradeDate"

aaa = FinanceData(ticker)
fileLocation = PureWindowsPath(r"C:\\Python\\")
print(fileLocation)

spy = yf.Ticker(ticker)
askPrice = yf.Ticker(ticker).info.get('ask')
bidPrice = yf.Ticker(ticker).info.get('bid')

todayDate = datetime.today().strftime('%Y-%m-%d')


optionExpireDates = yf.Ticker(ticker).options
optionChain = spy.option_chain('2023-01-20')

for expireDate in optionExpireDates:
    aaa = expireDate

spyCalls = pd.DataFrame(optionChain.calls)
spyPuts = pd.DataFrame(optionChain.puts)

spyCalls.drop(droppedColumnName, axis=1, inplace=True)
spyPuts.drop(droppedColumnName, axis=1, inplace=True)


writer = pd.ExcelWriter(filePath, engine='openpyxl')
spyCalls.to_excel(writer, sheet_name='spyCalls')
spyPuts.to_excel(writer, sheet_name='spyPuts')

writer.close()


#df.to_excel(filePath, sheet_name='spyCalls', index=False, header=True)

#df = pd.DataFrame(opt.puts)
#df.to_excel(filePath, sheet_name='spyPuts', index=False, header=True)
#print(df)

