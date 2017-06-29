#Self explanatory :)
from pandas_datareader import data as panda_reader
import fix_yahoo_finance as yf
from datetime import datetime, timedelta
from dataretrieval.data_retriever import DataRetriever
import numpy as np

class HistoricalDataRetriever(DataRetriever):
    def __init__(self) :
        self.bkk_stock_suffix = ".BK"

    def read_data_as_dataframe(self, stock_name, num_days = 400,
                               source = 'yahoo') :
        return self.__read_from_yahoo(stock_name, num_days)

    def __read_from_yahoo(self, stock_name, num_days) :
        bkk_stock_name = stock_name + self.bkk_stock_suffix

        end_date = datetime.today()
        start_date = end_date - timedelta(days = num_days)

        stock_data = panda_reader.get_data_yahoo(
                    bkk_stock_name, start = start_date,
                    end=end_date)

        # Returns data with columns : Open High Low Close Adj Close Volume
        return stock_data

    #Implement data reading from Siamchart.com
    def __read_from_siamchart(self) :
        pass
