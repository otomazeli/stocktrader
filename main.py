from dataretrieval.historical_data_retriever import HistoricalDataRetriever
from dataprocessing.historical_data_processor import HistoricalDataProcessor

def main() :
    historical_data_reader = HistoricalDataRetriever()
    historical_data_processor = HistoricalDataProcessor()
    stock_data = historical_data_reader.read_data_as_dataframe(stock_name = 'BEC')
    print(stock_data)

main()
