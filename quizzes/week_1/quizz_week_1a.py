import numpy as np
import pandas as pd
from colorama import init, Fore, Back, Style


def annualized_return(returns, periods_per_year):
    compounded_growth = (1 + returns).prod()
    n_periods = returns.shape[0]
    return compounded_growth ** (periods_per_year / n_periods) - 1


def annualized_volatility(returns, periods_per_year):
    annual_volatility = returns.std() * np.sqrt(periods_per_year)
    return annual_volatility


def maximum_drawdown(returns):
    cumulative_returns = (1 + returns).cumprod()
    previous_peaks = cumulative_returns.cummax()
    drawdowns = (cumulative_returns - previous_peaks) / previous_peaks
    return drawdowns.min()


def maximum_drawdown_period(returns):
    cumulative_returns = (1 + returns).cumprod()
    previous_peaks = cumulative_returns.cummax()
    drawdowns = (cumulative_returns - previous_peaks) / previous_peaks
    return drawdowns.idxmin()


def maximum_drawdown_3(returns):
    wealth_index = 1000 * (1 + returns / 100).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks) / previous_peaks
    return drawdowns.min()

init()

file = '/Users/javier/PycharmProjects/edhec/venv/data/Portfolios_Formed_on_ME_monthly_EW.csv'

me_m = pd.read_csv(file,
                   header=0, index_col=0, na_values=-99.99)
returns = me_m[['Lo 20', 'Hi 20']]
returns = returns / 100
returns.index = pd.to_datetime(returns.index, format="%Y%m").to_period('M')

lo_20 = returns['Lo 20']
hi_20 = returns['Hi 20']

lo_20_1999_2005 = lo_20['1999':'2015']
hi_20_1999_2005 = hi_20['1999':'2015']


def annual_return(portfolio, question_number):
    annualized_return_value = annualized_return(portfolio, 12)
    print(Fore.BLUE +"Question " + str(question_number) + Fore.RESET + ": The annualized return of the portfolio portfolio is: " + Fore.GREEN+str(
        round(annualized_return_value * 100, 2)) + "%")


def annual_volatility(portfolio, question_number):
    annualized_volatility_value = annualized_volatility(portfolio, 12)
    print(Fore.BLUE +"Question " + str(question_number) + Fore.RESET + ": The annualized volatility of the portfolio portfolio is: " + Fore.GREEN+str(
        round(annualized_volatility_value * 100, 2)) + "%")


def max_drawdown(portfolio, question_number):
    max_drawdown_value = maximum_drawdown(portfolio)
    print(Fore.BLUE + "Question " + str(question_number) + Fore.RESET + ": The maximum drawdown of the portfolio portfolio is: " + Fore.GREEN+str(
        round(max_drawdown_value * 100, 2)) + "%")


def max_drawdown_period(portfolio, question_number):
    max_drawdown_period_value = maximum_drawdown_period(portfolio)
    print(Fore.BLUE + "Question " + str(question_number) +  Fore.RESET +f": The maximum drawdown period of the portfolio is: " + Fore.GREEN+str(
        max_drawdown_period_value))


# qestion 1 - Lo 20 Returns

annual_return(lo_20, 1)

# question 2 - Lo 20 Volatility
annual_volatility(lo_20, 2)

# question 3 - Hi 20 Returns
annual_return(hi_20, 3)

# question 4 - Hi 20 Volatility
annual_volatility(hi_20, 4)

# question 5 - Lo 20 1999-2005 Returns

annual_return(lo_20_1999_2005, 5)

# question 6 - Lo 20 1999-2005 Volatility

annual_volatility(lo_20_1999_2005, 6)

# question 7 - Hi 20 1999-2005 Returns

annual_return(hi_20_1999_2005, 7)

# question 8 - Hi 20 1999-2005 Volatility

annual_volatility(hi_20_1999_2005, 8)

# question 9 - Lo 20 1999-2005 Max Drawdown
max_drawdown(lo_20_1999_2005, 9)

# question 10 - Lo 20 1999-2005 Max Drawdown Period
max_drawdown_period(lo_20_1999_2005, 10)

# question 11 - Hi 20 1999-2005 Max Drawdown
max_drawdown(hi_20_1999_2005, 11)

# question 12 - Hi 20 1999-2005 Max Drawdown Period
max_drawdown_period(hi_20_1999_2005, 12)
