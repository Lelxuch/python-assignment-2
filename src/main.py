import requests
from bs4 import BeautifulSoup

class Scrapper():
  def refactoreCoinName(self, coin): # For example "Binance Coin" -> "binance-coin"
    result = str(coin.lower())
    splittedCoin = result.split()
    if len(splittedCoin) > 1:
      result = str(splittedCoin[0])
      for i in range(1, len(splittedCoin)):
        result += "-" + splittedCoin[i]
    return result

  def getCryptoData(self, coin):
    result = []
    url = "https://coinmarketcap.com/currencies/"
    refactoredCoin = self.refactoreCoinName(coin)
    response = requests.get(url + refactoredCoin)
    html = BeautifulSoup(response.text, 'html.parser')
    for p in html.find_all('p'):
      result.append(p.get_text())
    return result

  def getTrending(self):
    result = []
    url = "https://coinmarketcap.com/trending-cryptocurrencies/"
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    for p in html.find_all('td'):
      result.append(p.get_text())
    return result

  def getGainersLosers(self):
    result = []
    url = "https://coinmarketcap.com/gainers-losers/"
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    for p in html.find_all('td'):
      result.append(p.get_text())
    return result

  def getNew(self):
    result = []
    url = "https://coinmarketcap.com/new/"
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    for p in html.find_all('td'):
      result.append(p.get_text())
    return result