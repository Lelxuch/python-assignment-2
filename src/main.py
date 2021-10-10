import requests
from bs4 import BeautifulSoup

class Scrapper():
  def getCryptoData(coin):
    result = []
    url = "https://coinmarketcap.com/currencies/"
    response = requests.get(url + coin)
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