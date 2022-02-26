import requests
import json

main_cur = input().lower()
cache = {main_cur: 1}
exchange_rates = requests.get(f"http://www.floatrates.com/daily/{main_cur}.json")
exchange_rates_json = json.loads(exchange_rates.text)


def cached(currency):
    global cache
    global main_cur
    global exchange_rates_json
    if currency not in cache:
        cache[currency] = exchange_rates_json[currency.lower()]['rate']


cached("usd")
cached("eur")
# print(exchange_rates_json)

while True:
    current = input().lower()
    if current == "":
        break
    money = float(input())
    print("Checking the cache...")
    if current in cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cached(current)
    rate = cache[current]
    exchanged_money = money * rate
    print(f"You received {exchanged_money} {current}")
