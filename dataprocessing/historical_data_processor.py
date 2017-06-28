from data_retriever import DataProcessor
class HistoricalDataProcessor(DataProcessor):
    def transform_data(self, dataframe) :
        yahoo_dataframe_columns = list(dataframe.columns.values)
        pass
