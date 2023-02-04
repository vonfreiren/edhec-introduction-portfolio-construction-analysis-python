import numpy as np
import pandas as pd
from colorama import Fore, init

from other.edhec_kit import skewness

file = '/Users/javier/PycharmProjects/edhec/venv/data/edhec-hedgefundindices.csv'
returns_file = pd.read_csv(file,
                           header=0, index_col=0, parse_dates=True)
returns_file = returns_file / 100
returns_file.index = returns_file.index.to_period('M')


def semi_deviation(returns):
    mean_returns = returns.mean()
    below_mean_returns = returns_file[returns_file < mean_returns]
    return np.std(below_mean_returns, ddof=0)


init()

returns_file_since_2009 = returns_file['2009':'2018']
returns_file_2000_2018 = returns_file.loc['2000':]
semideviations = returns_file_since_2009.apply(semi_deviation)

# Question 13

max_semideviation = semideviations.idxmax()[0]
print(Fore.BLUE + "Question 13: The maximum semideviation is: " + Fore.GREEN + max_semideviation)

# Question 14

min_semideviation = \
returns_file_since_2009[returns_file_since_2009 < returns_file_since_2009.mean()].std().sort_values().index[0]
print(Fore.BLUE + "Question 14: The minimum semideviation is: " + Fore.GREEN + min_semideviation)

# Question 15
skew = returns_file_since_2009.apply(skewness)
min_skew = skew.idxmin()
print(Fore.BLUE + "Question 15: The minimum skew is: " + Fore.GREEN + min_skew)

kurtosis = returns_file_2000_2018.kurtosis()

highest_kurtosis = kurtosis.idxmax()
# Question 16
print(Fore.BLUE + "Question 16: The kurtosis is: " + Fore.GREEN + str(highest_kurtosis))
