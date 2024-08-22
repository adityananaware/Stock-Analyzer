import requests
from bs4 import BeautifulSoup

def get_stock_fundamentals(stock_symbol):
    url = f"https://finance.yahoo.com/quote/{stock_symbol}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        pe_ratio = soup.find('td', {'data-test': 'PE_RATIO-value'}).text
    except AttributeError:
        pe_ratio = 'N/A'

    try:
        debt_equity_ratio = soup.find('td', {'data-test': 'DTE_RATIO-value'}).text
    except AttributeError:
        debt_equity_ratio = 'N/A'

    try:
        pb_ratio = soup.find('td', {'data-test': 'PB_RATIO-value'}).text
    except AttributeError:
        pb_ratio = 'N/A'

    try:
        roe = soup.find('td', {'data-test': 'ROE-value'}).text
    except AttributeError:
        roe = 'N/A'

    try:
        dividend_yield = soup.find('td', {'data-test': 'DIVIDEND_AND_YIELD-value'}).text
    except AttributeError:
        dividend_yield = 'N/A'

    try:
        market_capitalization = soup.find('td', {'data-test': 'MARKET_CAP-value'}).text
    except AttributeError:
        market_capitalization = 'N/A'

    return {
        'P/E Ratio': pe_ratio,
        'Debt/Equity Ratio': debt_equity_ratio,
        'P/B Ratio': pb_ratio,
        'ROE': roe,
        'Dividend Yield': dividend_yield,
        'Market Capitalization': market_capitalization
    }

if __name__ == "__main__":
    stock_symbol = input("Enter the stock symbol: ")
    fundamentals = get_stock_fundamentals(stock_symbol)
    for key, value in fundamentals.items():
        print(f"{key}: {value}")
