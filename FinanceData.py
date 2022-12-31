import yfinance as yf
import pandas as pd
from pathlib import Path, PureWindowsPath
from datetime import datetime

class FinanceData:

    def __init__(self, ticker):
        self.ticker = ticker

    def getAskPrice(self):
        askPrice = yf.Ticker(ticker).info.get('ask')
        return askPrice

    def getBidPrice(self):
        bidPrice = yf.Ticker(ticker).info.get('bid')
        return bidPrice
