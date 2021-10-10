import sys
sys.path.append('../src')
from main import Scrapper

scrapper = Scrapper()

while(True):
  print("Menu\n" +
  "1. Find cryptocurrency by name\n" +
  "2. Get trending cryptocurrencies\n" +
  "3. Get top gainers and losers\n" +
  "4. Get recently added\n" +
  "5. Exit")
  userSelect = int(input("Select option: "))
  if(userSelect == 1):
    cryptoName = input("Crypto name: ")
    for i in scrapper.getCryptoData(cryptoName):
      print(i)
  if(userSelect == 2):
    for i in scrapper.getTrending():
      print(i)
  if(userSelect == 3):
    gainersLosers = scrapper.getGainersLosers()
    for i in range(0, len(gainersLosers)):
      print(gainersLosers[i])
      if ((i + 1) % 5 == 0):
        print("\n")
  if(userSelect == 4):
    for i in scrapper.getNew():
      print(i)
  if(userSelect == 5 or userSelect > 5):
    print("Exit")
    break