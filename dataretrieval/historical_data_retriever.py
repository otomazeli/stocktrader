#Self explanatory :)

from pandas_datareader import data as panda_reader
import fix_yahoo_finance as yf
from datetime import datetime, timedelta
from data_retriever import DataRetriever

class HistoricalDataRetriever(DataRetriever):

    def __init__(self, path) :
        self.data_path = path
        self.bkk_stock_prefix = ".BK"

    def read_data_as_dataframe(self, stock_name, num_days = 90,
                               source = 'yahoo', path = None) :
        self.__read_from_yahoo(stock_name, num_days)

    def __read_from_yahoo(self, stock_name, num_days) :

        bkk_stock_name = stock_name + self.bkk_stock_prefix

        end_date = datetime.date.today()
        start_date = end_date - relativedelta(days = num_days)

        stock_data = panda_reader.get_data_yahoo(
                    bkk_stock_name, start = start_date,
                    end=end_date)

        stock_data

    #Implement data reading from Siamchart.com
    def __read_from_siamchart(self) :
        pass
    
