import numpy as np
import pandas as pd
class TechnicalCalculator :
    def __init__(self) :
        pass

    def calculate_moving_average(self, x, type='valid', n = 25):
        x = np.asarray(x)
        weights = np.exp(np.linspace(-1., 0., n))
        weights /= weights.sum()
        a = np.convolve(x, weights, mode='full')[:len(x)]
        a[:n] = a[n]
        return a

    def calculate_relative_strength_index(self, prices, n = 25):
        deltas = np.diff(prices)
        seed = deltas[:n+1]
        up = seed[seed >= 0].sum()/n
        down = -seed[seed < 0].sum()/n
        rs = up/down
        rsi = np.zeros_like(prices)
        rsi[:n] = 100. - 100./(1. + rs)

        for i in range(n, len(prices)):
            delta = deltas[i - 1]  # cause the diff is 1 shorter

            if delta > 0:
                upval = delta
                downval = 0.

            else:
                upval = 0.
                downval = -delta

            up = (up*(n - 1) + upval)/n
            down = (down*(n - 1) + downval)/n

            rs = up/down
            rsi[i] = 100. - 100./(1. + rs)

        return rsi

    def calculate_moving_average_convergence(self, x, nslow=26, nfast=12):
        emaslow = pd.ewma(x, nslow)
        emafast = pd.ewma(x, nfast)
        return emafast - emaslow

    def calculate_slow_stochastic(self, closing_prices, lows, highs, t = 25) :
        low, high = pd.rolling_min(closing_prices, t), pd.rolling_max(closing_prices, t)

        k = 100 * (closing_prices - low) / (high - low)
        return pd.rolling_mean(k,3)

    def calculate_r_percentage(self, closing_prices, lows, highs, t = 25) :
        low, high = pd.rolling_min(closing_prices, t), pd.rolling_max(closing_prices, t)

        r = 100 * (high - closing_prices)/(high - low)
        return r
