# python-assignment-2

Title: Assignment 2

This scrapper gets data from coinmarketcap.com

## Installation

PyPI
```bash
pip install requests
pip install beautifulsoup4
```

## Usage

Go to test folder and launch test.py
```bash
cd test
python3 test.py
```

## Examples

The user enters 1 and name of cryptocurrency. User can enter splitted words. My package connects them into one with a dash to get information from coinmarketcap.com

```
Menu
1. Find cryptocurrency  by name
2. Get trending cryptocurrencies
3. Get top gainers and losers
4. Get recently added
5. Exit
>>> Select option: 1
>>> Crypto name: Binance Coin
```

Output:

```
Information about cryptocurrency
```

The user enters 4 and gets the result:

```
Menu
1. Find cryptocurrency  by name
2. Get trending cryptocurrencies
3. Get top gainers and losers
4. Get recently added
5. Exit
>>> Select option: 4
```

Output:

```
1
PokerFI.Finance1POKERFI
$0.002383
7.94%
0.00%
$23,831,974
$2,720,404
Binance Coin
2 hours ago

2
SUPERLAUNCH2SLA
$0.1679
10.16%
0.00%
$1,679,065
$462,269
Binance Coin
5 hours ago

...
```
