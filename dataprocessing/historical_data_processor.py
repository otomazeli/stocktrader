from dataprocessing.data_processor import DataProcessor
import pandas as pd
from dataprocessing.technical.calculator import TechnicalCalculator

class HistoricalDataProcessor(DataProcessor):
    def transform_data(self, dataframe) :
        opens = dataframe['Open']
        highs = dataframe['High']
        lows = dataframe['Low']
        closing_prices = dataframe['Close']
        adj_close = dataframe['Adj Close']
        volumes = dataframe['Volume']

        calculator = TechnicalCalculator()

        moving_average = calculator.calculate_moving_average(closing_prices)
        rsi = calculator.calculate_relative_strength_index(closing_prices)
        macd = calculator.calculate_moving_average_convergence(closing_prices)
        kd = calculator.calculate_slow_stochastic(closing_prices, lows, highs)
        r_percentage = calculator.calculate_r_percentage(closing_prices, lows, highs)

        dataframe['ma'] = moving_average
        dataframe['rsi'] = rsi
        dataframe['macd'] = macd
        dataframe['kd'] = kd
        dataframe['r%'] = r_percentage

        return dataframe
