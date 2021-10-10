import sys
sys.path.append('../src')
from main import Scrapper

scrapper = Scrapper()

while(True):
  print("Menu\n" +
  "1. Find by name\n" +
  "2. Get trending cryptocurrencies\n" +
  "3. Get top gainers and losers\n"
  "4. Exit")
  userSelect = int(input("Select option: "))
  if(userSelect == 1):
    cryptoName = input("Crypto name: ")
    for i in scrapper.getCryptoData(cryptoName):
      print(i)
  if(userSelect == 2):
    for i in scrapper.getTrending():
      print(i)
  if(userSelect == 3):
    for i in scrapper.getGainersLosers():
      print(j)
  if(userSelect == 4 or userSelect > 4):
    print("Exit")
    break